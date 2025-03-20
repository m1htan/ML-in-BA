import matplotlib
from PyQt6.uic.properties import QtWidgets
from mysql.connector import cursor

from MLinBA.Midterm_MLinBA.Model.Prepare.Statistic import Statistic

matplotlib.use("QtAgg")

from MLinBA.Final_MLinBA.UI.LoginWindowExt import LoginWindowExt
from MLinBA.Final_MLinBA.UI.MainWindow import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QApplication

class MainWindowExt(QMainWindow, Statistic):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()

        self.LoginWindowExt=LoginWindowExt()
        self.LoginWindowExt.parent=self

    def initUI(self):
        # Kết nối các nút với hàm xử lý sự kiện
        self.ui.actionConnect_Database.triggered.connect(self.openDatabaseConnectUI)
        self.ui.actionExit.triggered.connect(self.processExit)

        # Kết nối các nút bấm
        self.ui.pushButton_1.clicked.connect(self.process1)
        self.ui.pushButton_2.clicked.connect(self.process2)
        self.ui.pushButton_3.clicked.connect(self.process3)
        self.ui.pushButton_4.clicked.connect(self.process4)
        self.ui.pushButton_5.clicked.connect(self.process5)

        self.ui.pushButtonPredict.clicked.connect(self.processPrediction)

    def showDataIntoTableWidget(self, table):
        table_name = self.comboBoxChooseTable.currentText()

        # Truy vấn dữ liệu từ bảng được chọn
        query = f"SELECT * FROM {table_name}"
        cursor.execute(query)
        data = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]

        # Cập nhật QTableWidget
        self.tableWidget.setRowCount(0)  # Xóa dữ liệu cũ
        self.tableWidget.setColumnCount(len(column_names))  # Cập nhật số cột

        # Gán tên cột
        for i, column_name in enumerate(column_names):
            self.tableWidget.setHorizontalHeaderItem(i, QTableWidgetItem(column_name))

        # Thêm dữ liệu vào QTableWidget
        for row_idx, row_data in enumerate(data):
            self.tableWidget.insertRow(row_idx)
            for col_idx, cell_data in enumerate(row_data):
                self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(cell_data)))

    def load_data(self):
        try:
            self.data = self.df
            self.tableWidget.setRowCount(len(self.data))
            self.tableWidget.setColumnCount(len(self.data.columns))
            self.tableWidget.setHorizontalHeaderLabels(self.data.columns)

            for i, row in self.data.iterrows():
                for j, value in enumerate(row):
                    self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(value)))

        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Không thể tải dữ liệu: {e}")

    def showWindow(self):
        self.showWindow()

    def openDatabaseConnectUI(self):
        self.dbwindow = QMainWindow()
        self.LoginWindowExt.setupUi(self.dbwindow)
        self.dbwindow.show()

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