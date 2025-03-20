import matplotlib
from PyQt6.uic.properties import QtWidgets

from Connectors.Connector import Connector
from Model.Prepare.Statistic import Statistic

matplotlib.use("QtAgg")

from UI.LoginWindowExt import LoginWindowExt
from UI.MainWindow import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QApplication

class MainWindowExt(QMainWindow, Statistic):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()
        self.conn=None

        self.LoginWindowExt=LoginWindowExt()
        self.LoginWindowExt.parent=self

    def initUI(self):
        # Kết nối các nút với hàm xử lý sự kiện
        self.ui.actionConnect_Database.triggered.connect(self.openDatabaseConnectUI)
        self.ui.actionExit.triggered.connect(self.processExit)

        # Kết nối các nút bấm
        self.ui.pushButton_1.clicked.connect(self.getTotalSalesByProduct)
        self.ui.pushButton_2.clicked.connect(self.getTotalRevenueByCategory)
        self.ui.pushButton_3.clicked.connect(self.getTotalRevenueByCategoryAndMonth)
        self.ui.pushButton_4.clicked.connect(self.getEarlyDeliveredOrders)

        self.ui.pushButtonPredict.clicked.connect(self.processPrediction)

    def showDataIntoTableWidget(self):
        table_name = self.ui.comboBoxChooseTable.currentText()

        print("Tên bảng được chọn:", table_name)  # Kiểm tra xem có lấy đúng không

        if not hasattr(self, 'connector') or self.connector is None:
            QMessageBox.critical(self, "Lỗi", "Chưa có kết nối đến cơ sở dữ liệu!")
            return

        if not table_name:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng chọn bảng trước!")
            return

        try:
            query = f"SELECT * FROM {table_name}"
            result_df = self.connector.queryDataset(query)  # Gọi hàm queryDataset()

            print("Dữ liệu từ query:", result_df)  # Kiểm tra dữ liệu trả về từ query

            if result_df is None or result_df.empty:
                QMessageBox.information(self, "Thông báo", f"Bảng {table_name} không có dữ liệu.")
                self.ui.tableWidget.setRowCount(0)
                return

            # Xóa dữ liệu cũ
            self.ui.tableWidget.clearContents()
            self.ui.tableWidget.setRowCount(0)
            self.ui.tableWidget.setColumnCount(len(result_df.columns))
            self.ui.tableWidget.setHorizontalHeaderLabels(result_df.columns)

            # Thêm dữ liệu vào QTableWidget
            for i, row in result_df.iterrows():
                self.ui.tableWidget.insertRow(i)
                for j, value in enumerate(row):
                    self.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(value)))

        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi khi tải dữ liệu: {str(e)}")

    def load_data(self):
        try:
            self.data = self.df
            self.ui.tableWidget.setRowCount(len(self.data))
            self.ui.tableWidget.setColumnCount(len(self.data.columns))
            self.ui.tableWidget.setHorizontalHeaderLabels(self.data.columns)

            for i, row in self.data.iterrows():
                for j, value in enumerate(row):
                    self.ui.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(value)))

        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Không thể tải dữ liệu: {e}")

    def showWindow(self):
        self.show()

    def openDatabaseConnectUI(self):
        self.LoginWindowExt.show()

    def processExit(self):
        reply = QMessageBox.question(
            self,
            "Xác nhận thoát",
            "Bạn có chắc chắn muốn thoát chương trình?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            QApplication.quit()

    # Câu 2: Viết lệnh và thực thi việc thống kê tổng doanh số bán hàng của các mặt hàng do khách hàng mua
    def getTotalSalesByProduct(self):
        query = """
        SELECT 
            c.CustomerID,
            c.FirstName,
            c.LastName,
            SUM(od.OrderQty * od.UnitPrice) AS TotalSales
        FROM orders o
        JOIN orderdetails od ON o.OrderID = od.OrderID
        JOIN customer c ON o.CustomerID = c.CustomerID
        GROUP BY c.CustomerID, c.FirstName, c.LastName
        ORDER BY TotalSales DESC;
        """
        return self.queryDataset(query)

    # Câu 3: Thống kê tổng doanh thu theo từng danh mục
    def getTotalRevenueByCategory(self):
        query = """
        SELECT 
            c.Name AS CategoryName,
            SUM(od.OrderQty * od.UnitPrice) AS TotalRevenue
        FROM orderdetails od
        JOIN product p ON od.ProductID = p.ProductID
        JOIN subcategory sc ON p.ProductSubcategoryID = sc.SubcategoryID
        JOIN category c ON sc.CategoryID = c.CategoryID
        GROUP BY c.Name
        ORDER BY TotalRevenue DESC;
        """
        return self.queryDataset(query)

    # Câu 4: Thống kê tổng doanh thu theo danh mục, phân theo Tháng + Năm
    def getTotalRevenueByCategoryAndMonth(self):
        query = """
        SELECT c.Name AS CategoryName, 
               DATE_FORMAT(STR_TO_DATE(o.OrderDate, '%d/%m/%Y'), '%Y-%m') AS YearMonth, 
               SUM(od.OrderQty * od.UnitPrice) AS TotalRevenue
        FROM orderdetails od
        JOIN orders o ON od.OrderID = o.OrderID
        JOIN product p ON od.ProductID = p.ProductID
        JOIN subcategory s ON p.ProductSubcategoryID = s.SubcategoryID
        JOIN category c ON s.CategoryID = c.CategoryID
        GROUP BY c.Name, YearMonth
        ORDER BY YearMonth;
        """
        return self.queryDataset(query)

    # Câu 5: Thống kê các đơn hàng được giao nhanh trước hạn từ 3 ngày trở lên
    def getEarlyDeliveredOrders(self):
        query = """
        SELECT OrderID, 
            STR_TO_DATE(OrderDate, '%d/%m/%Y') AS OrderDate, 
            STR_TO_DATE(DueDate, '%d/%m/%Y') AS DueDate, 
            STR_TO_DATE(ShipDate, '%d/%m/%Y') AS ShipDate,
            DATEDIFF(STR_TO_DATE(DueDate, '%d/%m/%Y'), STR_TO_DATE(ShipDate, '%d/%m/%Y')) AS DaysEarly
        FROM orders
        WHERE DATEDIFF(STR_TO_DATE(DueDate, '%d/%m/%Y'), STR_TO_DATE(ShipDate, '%d/%m/%Y')) >= 3;
        """
        return self.queryDataset(query)

    # Câu 6 Viết hàm để trả về thông tin chi tiết về Customer khi biết CustomerID.
    def getCustomerDetails(self, customerID):
        query = """SELECT * FROM customer WHERE CustomerID = {customerID};"""
        return self.queryDataset(query)

    # Câu 7: Viết hàm để trả về tất cả các Đơn hàng của Customer đã mua khi biết CustomerID
    def getCustomerOrders(self, customerID):
        query = """
        SELECT c.CustomerID, o.OrderID, o.OrderDate, o.DueDate, o.ShipDate, 
               p.Name AS ProductName, od.OrderQty, od.UnitPrice, 
               (od.OrderQty * od.UnitPrice) AS TotalPrice
        FROM orders o
        JOIN customer c on c.CustomerID = o.CustomerID
        JOIN orderdetails od ON o.OrderID = od.OrderID
        JOIN product p ON od.ProductID = p.ProductID
        WHERE o.CustomerID = {customerID};
        """
        return self.queryDataset(query)

    def processPrediction(self):
        pass