import pandas as pd
from PyQt6.uic.properties import QtWidgets
from matplotlib import pyplot as plt
from matplotlib.backends.backend_template import FigureCanvas

from MLinBA.Final_MLinBA.UI.MainWindow import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QFileDialog


class MainWindowExt(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        # Kết nối các nút với hàm xử lý sự kiện
        self.pushButtonCustomerAge.clicked.connect(self.show_customer_age)
        self.pushButtonAnnualPremium.clicked.connect(self.show_annual_premium)
        self.pushButtonByGenderAndVehicleDamage.clicked.connect(self.show_gender_vehicle_damage)
        self.pushButtonByAgeGroup.clicked.connect(self.show_age_group)
        self.pushButtonByVehicleAge.clicked.connect(self.show_vehicle_age)
        self.pushButton_LoadModel.clicked.connect(self.load_model)
        self.pushButton_TrainModel.clicked.connect(self.train_model)
        self.pushButtonPredict.clicked.connect(self.predict)
        self.pushButton_SaveModel.clicked.connect(self.save_model)

        # Load dữ liệu ban đầu
        self.data = None
        self.model = None

    def load_data(self, file_path):
        try:
            self.data = pd.read_csv(file_path)
            self.tableWidget_ListOfData.setRowCount(len(self.data))
            self.tableWidget_ListOfData.setColumnCount(len(self.data.columns))
            self.tableWidget_ListOfData.setHorizontalHeaderLabels(self.data.columns)

            for i, row in self.data.iterrows():
                for j, value in enumerate(row):
                    self.tableWidget_ListOfData.setItem(i, j, QtWidgets.QTableWidgetItem(str(value)))

        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Không thể tải dữ liệu: {e}")

    def show_chart(self, title, x, y):
        fig, ax = plt.subplots()
        ax.bar(x, y)
        ax.set_title(title)
        ax.set_xlabel("Danh mục")
        ax.set_ylabel("Số lượng")

        canvas = FigureCanvas(fig)
        for i in reversed(range(self.verticalLayout_ChartVisualization.count())):
            self.verticalLayout_ChartVisualization.itemAt(i).widget().setParent(None)

        self.verticalLayout_ChartVisualization.addWidget(canvas)

    def show_customer_age(self):
        if self.data is not None:
            age_counts = self.data['Customer_Age'].value_counts()
            self.show_chart("Customer Age Distribution", age_counts.index, age_counts.values)
        else:
            QMessageBox.warning(self, "Cảnh báo", "Chưa có dữ liệu để hiển thị!")

    def show_annual_premium(self):
        if self.data is not None:
            premium_counts = self.data['Annual_Premium'].value_counts()
            self.show_chart("Annual Premium Distribution", premium_counts.index, premium_counts.values)

    def show_gender_vehicle_damage(self):
        if self.data is not None:
            grouped_data = self.data.groupby(['Gender', 'Vehicle_Damage']).size().unstack()
            grouped_data.plot(kind='bar', stacked=True)
            plt.title("Gender vs Vehicle Damage")
            plt.xlabel("Gender")
            plt.ylabel("Count")
            plt.legend(title="Vehicle Damage")
            plt.show()

    def show_age_group(self):
        pass  # Tương tự show_customer_age

    def show_vehicle_age(self):
        pass  # Tương tự show_annual_premium

    def load_model(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Chọn mô hình", "", "Model Files (*.pkl)")
        if file_path:
            self.model = pd.read_pickle(file_path)
            QMessageBox.information(self, "Thành công", "Mô hình đã được tải thành công!")

    def train_model(self):
        if self.data is not None:
            QMessageBox.information(self, "Đang huấn luyện", "Huấn luyện mô hình... (chưa triển khai)")
        else:
            QMessageBox.warning(self, "Cảnh báo", "Chưa có dữ liệu để train!")

    def predict(self):
        if self.model is not None:
            QMessageBox.information(self, "Dự đoán", "Đang thực hiện dự đoán... (chưa triển khai)")
        else:
            QMessageBox.warning(self, "Cảnh báo", "Chưa tải mô hình!")

    def save_model(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Lưu mô hình", "", "Model Files (*.pkl)")
        if file_path:
            pd.to_pickle(self.model, file_path)
            QMessageBox.information(self, "Thành công", "Mô hình đã được lưu thành công!")

    def showWindow(self):
        self.show()
