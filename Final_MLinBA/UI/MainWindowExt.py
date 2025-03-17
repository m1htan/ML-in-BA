import matplotlib
import numpy as np
import pandas as pd
import seaborn as sns
from PyQt6.uic.properties import QtWidgets
from matplotlib import pyplot as plt
matplotlib.use("QtAgg")
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

from MLinBA.Final_MLinBA.Model.ML.WithOversampling.DecisionTree import DecisionTreeModelOversampling
from MLinBA.Final_MLinBA.Model.ML.WithOversampling.LogisticRegression import LogisticRegressionModelOversampling
from MLinBA.Final_MLinBA.Model.ML.WithOversampling.RandomForest import RandomForestModelOversampling
from MLinBA.Final_MLinBA.Model.ML.WithOversampling.XGBoost import XGBoostModelOversampling

from MLinBA.Final_MLinBA.Model.ML.WithoutOversampling.DecisionTree import DecisionTreeModel
from MLinBA.Final_MLinBA.Model.ML.WithoutOversampling.LogisticRegression import LogisticRegressionModel
from MLinBA.Final_MLinBA.Model.ML.WithoutOversampling.RandomForest import RandomForestModel
from MLinBA.Final_MLinBA.Model.ML.WithoutOversampling.XGBoost import XGBoostModel

from MLinBA.Final_MLinBA.Model.Prepare.PrepareData import df, DataProcessor
from MLinBA.Final_MLinBA.UI.LoginWindowExt import LoginWindowExt
from MLinBA.Final_MLinBA.UI.MainWindow import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QTableWidgetItem, QApplication


class MainWindowExt(QMainWindow, Ui_MainWindow, DataProcessor):
    def __init__(self):
        super().__init__()
        self.Ui_MainWindow = Ui_MainWindow()
        self.QMainWindow=QMainWindow()
        self.setupUi(self)
        self.initUI()
        self.LoginWindowExt=LoginWindowExt()
        self.LoginWindowExt.parent=self

        self.DecisionTreeModelOversampling = DecisionTreeModelOversampling()
        self.LogisticRegressionModelOversampling = LogisticRegressionModelOversampling()
        self.RandomForestModelOversampling = RandomForestModelOversampling()
        self.XGBoostModelOversampling = XGBoostModelOversampling()

        self.DecisionTreeModel = DecisionTreeModel()
        self.LogisticRegressionModel = LogisticRegressionModel()
        self.RandomForestModel = RandomForestModel()
        self.XGBoostModel = XGBoostModel()
        self.df=df

    def setupUi(self, MainWindow):
        Ui_MainWindow.setupUi(self, MainWindow)

        self.pushButtonSavePath_LR.clicked.connect(self.processPickSavePath)
        self.pushButtonSavePath_DT.clicked.connect(self.processPickSavePath)
        self.pushButtonSavePath_RF.clicked.connect(self.processPickSavePath)
        self.pushButtonSavePath_XGBoost.clicked.connect(self.processPickSavePath)

        self.pushButton_SaveModel_LR.clicked.connect(self.processSaveTrainedModel)
        self.pushButton_SaveModel_DT.clicked.connect(self.processSaveTrainedModel)
        self.pushButton_SaveModel_RF.clicked.connect(self.processSaveTrainedModel)
        self.pushButton_SaveModel_XGBoost.clicked.connect(self.processSaveTrainedModel)

        self.pushButton_TrainModel_LR.clicked.connect(self.processTrainModel_and_Evaluate_LR)
        self.pushButton_TrainModel_DT.clicked.connect(self.processTrainModel_and_Evaluate_DT)
        self.pushButton_TrainModel_RF.clicked.connect(self.processTrainModel_and_Evaluate_RF)
        self.pushButton_TrainModel_XGBoost.clicked.connect(self.processTrainModel_and_Evaluate_XG)

        self.pushButtonPredict_DT.clicked.connect(self.processPrediction_DT)
        self.pushButtonPredict_LR.clicked.connect(self.processPrediction_LR)
        self.pushButtonPredict_RF.clicked.connect(self.processPrediction_RF)
        self.pushButtonPredict_XGBoost.clicked.connect(self.processPrediction_XG)

    def initUI(self):
        # Kết nối các nút với hàm xử lý sự kiện
        self.actionConnect_Database.triggered.connect(self.openDatabaseConnectUI)
        self.actionExit.triggered.connect(self.processExit)

        # Overview Statistics
        self.pushButtonTotalNumberOfCustomer.clicked.connect(self.TotalNumberOfCustomer)
        self.pushButtonMaleFemaleRatio.clicked.connect(self.MaleFemaleRatio)
        self.pushButtonAverageCustomerAge.clicked.connect(self.AverageCustomerAge)
        self.pushButtonCusWithLicense.clicked.connect(self.CusWithLicense)
        self.pushButtonInsuaranceBuyers.clicked.connect(self.InsuaranceBuyers)

        # Customer Behavior
        self.pushButtonDistributionOfVehicleAge.clicked.connect(self.DistributionOfVehicleAge)
        self.pushButtonCusWithVehicleDamage.clicked.connect(self.CusWithVehicleDamage)
        self.pushButtonApprovalRate.clicked.connect(self.ApprovalRate)

        # Regional Analysis
        self.pushButtonTopCusRegions.clicked.connect(self.TopCusRegions)
        self.pushButtonTopResponsiveRegions.clicked.connect(self.TopResponsiveRegions)

        # Load dữ liệu ban đầu
        self.data = df
        self.model = (DecisionTreeModelOversampling, DecisionTreeModel,
                      LogisticRegressionModelOversampling, LogisticRegressionModel,
                      RandomForestModelOversampling, RandomForestModel,
                      XGBoostModelOversampling, XGBoostModel)

    def TotalNumberOfCustomer(self):
        self.check_data_empty()
        total_customers = len(self.df)

        # Tạo DataFrame để hiển thị
        df_display = pd.DataFrame({"Tổng khách hàng": [total_customers]})

        # Hiển thị dữ liệu trên bảng
        self.showDataIntoTableWidget(df_display)

        # Hiển thị biểu đồ cột
        self.show_chart(title="Tổng số khách hàng", x=["Tổng khách hàng"], y=[total_customers], chart_type="bar")

    def MaleFemaleRatio(self):
        self.check_data_empty()

        # Lấy dữ liệu giới tính từ DataFrame
        gender_counts = self.df['Gender'].value_counts(dropna=True)

        # Tạo DataFrame để hiển thị
        df_display = pd.DataFrame({
            "Giới tính": ["Nam", "Nữ"],
            "Số lượng": [gender_counts.get(0, 0), gender_counts.get(1, 0)]
        })

        # Hiển thị dữ liệu trên bảng
        self.showDataIntoTableWidget(df_display)

        labels = ["Nam" if x == 0 else "Nữ" for x in gender_counts.index.tolist()]
        sizes = gender_counts.values.tolist()

        # Tạo Figure và vẽ biểu đồ
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['#66b3ff', '#ff9999'])
        ax.set_title('Tỷ lệ Nam - Nữ')

        # Xóa biểu đồ cũ nếu có
        for i in reversed(range(self.verticalLayout_ChartVisualization.count())):
            self.verticalLayout_ChartVisualization.itemAt(i).widget().setParent(None)

        # Hiển thị biểu đồ trên PyQt
        canvas = FigureCanvas(fig)
        self.verticalLayout_ChartVisualization.addWidget(canvas)

    def AverageCustomerAge(self):
        self.check_data_empty()

        # Xóa biểu đồ cũ trước khi vẽ mới
        for i in reversed(range(self.verticalLayout_ChartVisualization.count())):
            self.verticalLayout_ChartVisualization.itemAt(i).widget().setParent(None)

        # Lấy giá trị trung bình tuổi khách hàng
        avg_age = round(self.df['Age'].mean(), 2)

        # Tạo DataFrame để hiển thị
        df_display = pd.DataFrame({"Tuổi trung bình": [avg_age]})

        # Hiển thị dữ liệu trên bảng
        self.showDataIntoTableWidget(df_display)

        # Tạo Figure và Axes mới
        fig, ax = plt.subplots(figsize=(8, 6))

        # Vẽ biểu đồ phân bố tuổi khách hàng
        sns.histplot(self.df['Age'], bins=20, kde=True, color='blue', ax=ax)
        ax.axvline(avg_age, color='red', linestyle='dashed', linewidth=2, label=f'Trung bình: {avg_age}')
        ax.set_title('Phân bố tuổi khách hàng')
        ax.set_xlabel('Tuổi')
        ax.set_ylabel('Số lượng')
        ax.legend()

        # Chuyển Figure thành Canvas để hiển thị trên PyQt
        canvas = FigureCanvas(fig)
        self.verticalLayout_ChartVisualization.addWidget(canvas)

        return avg_age  # Trả về giá trị tuổi trung bình

    def CusWithLicense(self):
        self.check_data_empty()

        # Xóa biểu đồ cũ trước khi vẽ mới
        for i in reversed(range(self.verticalLayout_ChartVisualization.count())):
            self.verticalLayout_ChartVisualization.itemAt(i).widget().setParent(None)

        # Lấy dữ liệu về bằng lái xe
        license_ratio = self.df['Driving_License'].value_counts(normalize=True) * 100
        yes_ratio = float(license_ratio.get(1, 0))
        no_ratio = float(license_ratio.get(0, 0))

        # Tạo DataFrame để hiển thị
        df_display = pd.DataFrame({
            "Tình trạng bằng lái": ["Có bằng lái", "Không có bằng lái"],
            "Tỷ lệ (%)": [license_ratio.get(1, 0), license_ratio.get(0, 0)]
        })

        # Hiển thị dữ liệu trên bảng
        self.showDataIntoTableWidget(df_display)

        # Dữ liệu để vẽ biểu đồ
        labels = ["Có bằng lái", "Không có bằng lái"]
        sizes = [yes_ratio, no_ratio]
        colors = ['#66b3ff', '#ff9999']

        # Tạo Figure và Axes mới
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
        ax.set_title('Tỷ lệ khách hàng có bằng lái')

        # Chuyển Figure thành Canvas để hiển thị trên PyQt
        canvas = FigureCanvas(fig)
        self.verticalLayout_ChartVisualization.addWidget(canvas)

        return {"Có bằng lái": round(yes_ratio, 2), "Không có bằng lái": round(no_ratio, 2)}


    def InsuaranceBuyers(self):
        self.check_data_empty()

        # Xóa biểu đồ cũ trước khi vẽ mới
        for i in reversed(range(self.verticalLayout_ChartVisualization.count())):
            self.verticalLayout_ChartVisualization.itemAt(i).widget().setParent(None)

        # Lấy dữ liệu về người từng mua bảo hiểm
        insured_ratio = self.df['Previously_Insured'].value_counts(normalize=True) * 100
        yes_ratio = float(insured_ratio.get(1, 0))
        no_ratio = float(insured_ratio.get(0, 0))

        # Tạo DataFrame để hiển thị
        df_display = pd.DataFrame({
            "Tình trạng bảo hiểm": ["Đã từng mua", "Chưa từng mua"],
            "Tỷ lệ (%)": [insured_ratio.get(1, 0), insured_ratio.get(0, 0)]
        })

        # Hiển thị dữ liệu trên bảng
        self.showDataIntoTableWidget(df_display)

        # Dữ liệu để vẽ biểu đồ
        labels = ["Đã từng mua", "Chưa từng mua"]
        sizes = [yes_ratio, no_ratio]
        colors = ['#66b3ff', '#ff9999']

        # Tạo Figure và Axes mới
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
        ax.set_title('Tỷ lệ khách hàng đã từng mua bảo hiểm')

        # Chuyển Figure thành Canvas để hiển thị trên PyQt
        canvas = FigureCanvas(fig)
        self.verticalLayout_ChartVisualization.addWidget(canvas)

        return {"Đã từng mua": round(yes_ratio, 2), "Chưa từng mua": round(no_ratio, 2)}

    def DistributionOfVehicleAge(self):
        self.check_data_empty()  # Kiểm tra dữ liệu rỗng

        # Xóa biểu đồ cũ trước khi vẽ mới
        for i in reversed(range(self.verticalLayout_ChartVisualization.count())):
            self.verticalLayout_ChartVisualization.itemAt(i).widget().setParent(None)

        mapping = {0: 'Dưới 1 năm', 1: '1-2 năm', 2: 'Trên 2 năm'}
        df_temp = self.df.copy()  # Tạo bản sao để tránh thay đổi dữ liệu gốc
        df_temp['Vehicle_Age'] = df_temp['Vehicle_Age'].astype(int).map(mapping)

        # Kiểm tra nếu sau ánh xạ còn NaN
        if df_temp['Vehicle_Age'].isna().sum() > 0:
            QMessageBox.warning(self, "Lỗi", "Dữ liệu tuổi xe không hợp lệ hoặc có giá trị rỗng!")
            return

        # Tính toán tỷ lệ phần trăm của từng nhóm tuổi xe
        vehicle_age_counts = df_temp['Vehicle_Age'].value_counts(normalize=True) * 100
        age_categories = ['Dưới 1 năm', '1-2 năm', 'Trên 2 năm']

        # Đảm bảo `values` có đúng 3 phần tử
        values = [round(vehicle_age_counts.get(cat, 0.0), 2) for cat in age_categories]

        # Kiểm tra nếu tất cả giá trị bằng 0
        if sum(values) == 0:
            QMessageBox.warning(self, "Lỗi", "Không có dữ liệu hợp lệ để vẽ biểu đồ!")
            return

        # Kiểm tra kích thước của danh sách
        if len(age_categories) != len(values):
            QMessageBox.warning(self, "Lỗi", "Số lượng danh mục không khớp với số lượng giá trị!")
            return

        # Tạo DataFrame để hiển thị
        df_display = pd.DataFrame({
            "Tuổi xe": age_categories,
            "Tỷ lệ (%)": values
        })

        # Hiển thị dữ liệu trên bảng
        self.showDataIntoTableWidget(df_display)

        # Tạo Figure và Axes mới
        fig, ax = plt.subplots(figsize=(8, 6))
        bars = ax.bar(age_categories, values, color=['#66b3ff', '#ff9999', '#99ff99'])

        # Thêm tiêu đề & nhãn trục
        ax.set_title('Phân bố tuổi xe', fontsize=14, fontweight='bold')
        ax.set_ylabel('Tỷ lệ (%)', fontsize=12)

        # Hiển thị giá trị trên từng cột
        for bar, value in zip(bars, values):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, f"{value}%", ha='center', fontsize=10,
                    fontweight='bold')

        # Chuyển Figure thành Canvas để hiển thị trên PyQt
        canvas = FigureCanvas(fig)
        self.verticalLayout_ChartVisualization.addWidget(canvas)

        return dict(zip(age_categories, values))

    def CusWithVehicleDamage(self):
        self.check_data_empty()  # Kiểm tra dữ liệu rỗng

        # Xóa biểu đồ cũ trước khi vẽ mới
        for i in reversed(range(self.verticalLayout_ChartVisualization.count())):
            self.verticalLayout_ChartVisualization.itemAt(i).widget().setParent(None)

        # Chuyển Vehicle_Damage về kiểu số (tránh lỗi khi `.get()`)
        self.df['Vehicle_Damage'] = self.df['Vehicle_Damage'].astype(int)

        # Lấy dữ liệu về tổn thất xe
        damage_ratio = self.df['Vehicle_Damage'].value_counts(normalize=True) * 100
        categories = ["Từng gặp tổn thất", "Chưa gặp tổn thất"]
        values = [
            round(float(damage_ratio.get(1, 0.0)), 2),
            round(float(damage_ratio.get(0, 0.0)), 2)
        ]

        # Kiểm tra nếu tất cả giá trị bằng 0
        if sum(values) == 0:
            QMessageBox.warning(self, "Lỗi", "Không có dữ liệu hợp lệ để vẽ biểu đồ!")
            return

        # Kiểm tra kích thước danh sách trước khi vẽ
        if len(categories) != len(values):
            QMessageBox.warning(self, "Lỗi", "Số lượng danh mục không khớp với số lượng giá trị!")
            return

        # Tạo DataFrame để hiển thị
        df_display = pd.DataFrame({
            "Tình trạng tổn thất": ["Từng gặp tổn thất", "Chưa gặp tổn thất"],
            "Tỷ lệ (%)": [damage_ratio.get(1, 0.0), damage_ratio.get(0, 0.0)]
        })

        # Hiển thị dữ liệu trên bảng
        self.showDataIntoTableWidget(df_display)

        # Tạo Figure và Axes mới
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.pie(values, labels=categories, autopct='%1.1f%%', colors=['#ff6666', '#66b3ff'])
        ax.set_title('Tỷ lệ tổn thất xe')

        # Chuyển Figure thành Canvas để hiển thị trên PyQt
        canvas = FigureCanvas(fig)
        self.verticalLayout_ChartVisualization.addWidget(canvas)

        return dict(zip(categories, values))

    def ApprovalRate(self):
        self.check_data_empty()

        # Xóa biểu đồ cũ trước khi vẽ mới
        for i in reversed(range(self.verticalLayout_ChartVisualization.count())):
            self.verticalLayout_ChartVisualization.itemAt(i).widget().setParent(None)

        # Lấy dữ liệu về tỷ lệ khách hàng đồng ý mua bảo hiểm
        response_ratio = self.df['Response'].value_counts(normalize=True) * 100
        categories = ["Đồng ý mua", "Không đồng ý"]
        values = [
            round(float(response_ratio.get(1, 0)), 2),
            round(float(response_ratio.get(0, 0)), 2)
        ]

        # Tạo DataFrame để hiển thị
        df_display = pd.DataFrame({
            "Phản hồi": ["Đồng ý mua", "Không đồng ý"],
            "Tỷ lệ (%)": [response_ratio.get(1, 0), response_ratio.get(0, 0)]
        })

        # Hiển thị dữ liệu trên bảng
        self.showDataIntoTableWidget(df_display)

        # Tạo Figure và Axes mới
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.pie(values, labels=categories, autopct='%1.1f%%', colors=['#99ff99', '#ff6666'])
        ax.set_title('Tỷ lệ khách hàng đồng ý mua bảo hiểm')

        # Chuyển Figure thành Canvas để hiển thị trên PyQt
        canvas = FigureCanvas(fig)
        self.verticalLayout_ChartVisualization.addWidget(canvas)

        return dict(zip(categories, values))

    def TopCusRegions(self, top_n=5):
        self.check_data_empty()  # Kiểm tra dữ liệu rỗng
        self.top_n=top_n

        # Kiểm tra nếu 'Region_Code' không tồn tại hoặc rỗng
        if 'Region_Code' not in self.df.columns or self.df['Region_Code'].isna().all():
            QMessageBox.warning(self, "Lỗi", "Dữ liệu khu vực không hợp lệ hoặc trống!")
            return

        # Đảm bảo `Region_Code` là kiểu số nguyên
        self.df['Region_Code'] = pd.to_numeric(self.df['Region_Code'], errors='coerce')

        # Xóa biểu đồ cũ trước khi vẽ mới
        for i in reversed(range(self.verticalLayout_ChartVisualization.count())):
            self.verticalLayout_ChartVisualization.itemAt(i).widget().setParent(None)

        # Lấy danh sách top N khu vực có nhiều khách hàng nhất
        region_counts = self.df['Region_Code'].value_counts()

        # Tính tỷ lệ phần trăm
        total_customers = len(self.df)
        region_ratios = (region_counts / total_customers * 100).round(2)

        # Chuẩn bị dữ liệu cho biểu đồ
        labels = [str(k) for k in region_ratios.index]
        values = [float(v) for v in region_ratios.values]

        # Nếu không có dữ liệu hợp lệ thì dừng
        if not values:
            QMessageBox.warning(self, "Lỗi", "Không có dữ liệu hợp lệ để vẽ biểu đồ!")
            return

        # Dữ liệu hiển thị
        df_display = pd.DataFrame({
            "Mã vùng": [str(k) for k in region_ratios.index],
            "Tỷ lệ khách hàng (%)": [float(v) for v in region_ratios.values]
        })

        # Hiển thị dữ liệu trên bảng
        self.showDataIntoTableWidget(df_display)

        # Tạo Figure và Axes mới
        fig, ax = plt.subplots(figsize=(8, 6))
        bars = ax.bar(labels, values, color=sns.color_palette("viridis", len(labels)))

        ax.set_title(f'Top khu vực có nhiều khách hàng nhất', fontsize=14, fontweight='bold')
        ax.set_xlabel('Mã vùng', fontsize=12)
        ax.set_ylabel('Tỷ lệ khách hàng (%)', fontsize=12)

        # Chuyển Figure thành Canvas để hiển thị trên PyQt
        canvas = FigureCanvas(fig)
        self.verticalLayout_ChartVisualization.addWidget(canvas)

        return dict(zip(labels, values))  # Trả về dữ liệu thống kê

    def TopResponsiveRegions(self, top_n=5):
        self.check_data_empty()  # Kiểm tra dữ liệu rỗng
        self.top_n=top_n

        # Xóa biểu đồ cũ trước khi vẽ mới
        for i in reversed(range(self.verticalLayout_ChartVisualization.count())):
            self.verticalLayout_ChartVisualization.itemAt(i).widget().setParent(None)

        # Tính tỷ lệ phản hồi của từng khu vực và lấy `top_n` khu vực có phản hồi cao nhất
        region_response = self.df.groupby('Region_Code')['Response'].mean() * 100
        region_response=region_response.sort_values(ascending=False)

        # Kiểm tra nếu không có dữ liệu hợp lệ
        if region_response.empty:
            QMessageBox.warning(self, "Lỗi", "Không có dữ liệu phản hồi hợp lệ để vẽ biểu đồ!")
            return

        # Chuẩn bị dữ liệu cho biểu đồ
        labels = [str(k) for k in region_response.index]
        values = [float(v) for v in region_response.values]

        # Nếu không có dữ liệu hợp lệ thì dừng
        if not values:
            QMessageBox.warning(self, "Lỗi", "Không có dữ liệu hợp lệ để vẽ biểu đồ!")
            return

        # Dữ liệu hiển thị
        df_display = pd.DataFrame({
            "Mã vùng": [str(k) for k in region_response.index],
            "Tỷ lệ phản hồi (%)": [float(v) for v in region_response.values]
        })

        # Hiển thị dữ liệu trên bảng
        self.showDataIntoTableWidget(df_display)

        # Tạo Figure và Axes mới
        fig, ax = plt.subplots(figsize=(8, 6))
        bars = ax.bar(labels, values, color=sns.color_palette("viridis", len(labels)))

        ax.set_title(f'Top khu vực có tỷ lệ phản hồi cao nhất', fontsize=14, fontweight='bold')
        ax.set_xlabel('Mã vùng', fontsize=12)
        ax.set_ylabel('Tỷ lệ phản hồi (%)', fontsize=12)
        ax.set_ylim(0, max(values) + 5)  # Điều chỉnh trục Y để hiển thị đẹp hơn

        # Chuyển Figure thành Canvas để hiển thị trên PyQt
        canvas = FigureCanvas(fig)
        self.verticalLayout_ChartVisualization.addWidget(canvas)

        # Trả về dữ liệu thống kê
        return dict(zip(labels, values))

    def load_data(self, df):
        try:
            self.data = df
            self.tableWidget_ListOfData.setRowCount(len(self.data))
            self.tableWidget_ListOfData.setColumnCount(len(self.data.columns))
            self.tableWidget_ListOfData.setHorizontalHeaderLabels(self.data.columns)

            for i, row in self.data.iterrows():
                for j, value in enumerate(row):
                    self.tableWidget_ListOfData.setItem(i, j, QtWidgets.QTableWidgetItem(str(value)))

        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Không thể tải dữ liệu: {e}")

    def openDatabaseConnectUI(self):
        self.dbwindow = QMainWindow()
        self.LoginWindowExt.setupUi(self.dbwindow)
        self.dbwindow.show()

    def showDataIntoTableWidget(self, df):
        self.tableWidget_ListOfData.setRowCount(0)  # Xóa dữ liệu cũ
        self.tableWidget_ListOfData.setColumnCount(len(df.columns))  # Cập nhật số cột

        for i in range(len(df.columns)):  # Gán tên cột
            columnHeader = df.columns[i]
            self.tableWidget_ListOfData.setHorizontalHeaderItem(i, QTableWidgetItem(columnHeader))

        row = 0
        for item in df.iloc:  # Duyệt từng dòng trong DataFrame
            arr = item.values.tolist()
            self.tableWidget_ListOfData.insertRow(row)
            j = 0
            for data in arr:
                self.tableWidget_ListOfData.setItem(row, j, QTableWidgetItem(str(data)))
                j += 1
            row += 1

    def show_chart(self, title, x, y, chart_type="bar"):
        fig, ax = plt.subplots()

        if chart_type == "bar":
            ax.bar(x, y, color=['blue', 'orange'])
        elif chart_type == "pie":
            ax.pie(y, labels=x, autopct='%1.1f%%', colors=['blue', 'orange'])

        ax.set_title(title)

        # Xóa biểu đồ cũ trước khi vẽ cái mới
        for i in reversed(range(self.verticalLayout_ChartVisualization.count())):
            self.verticalLayout_ChartVisualization.itemAt(i).widget().setParent(None)

        # Vẽ biểu đồ
        canvas = FigureCanvas(fig)
        self.verticalLayout_ChartVisualization.addWidget(canvas)

    def processTrainModel_and_Evaluate_LR(self):
        # Lấy lựa chọn từ comboBox
        selected_model = self.comboBox_LoadModel_RF.currentText()

        # Lấy dữ liệu từ giao diện người dùng
        test_size_lr = float(self.lineEdit_TestSize_LR.text()) / 100
        regularization_lr = float(self.lineEdit_C_LR.text())
        max_iter_lr = int(self.lineEdit_MaxIter_LR.text())

        # Khởi tạo mô hình phù hợp
        if selected_model == "With Oversampling":
            self.LogisticRegressionModel = LogisticRegressionModelOversampling(C=regularization_lr, max_iter_lr=max_iter_lr)
        else:
            self.LogisticRegressionModel = LogisticRegressionModel(C=regularization_lr, max_iter_lr=max_iter_lr)

        # Gọi prepare_data để tạo tập train/test theo test_size_lr
        self.LogisticRegressionModel.prepare_data(test_size=test_size_lr)

        # Huấn luyện mô hình
        self.LogisticRegressionModel.train()

        # Đánh giá mô hình
        result = self.LogisticRegressionModel.evaluate()

        # Hiển thị kết quả trên giao diện
        self.lineEdit_MAE_LR.setText(str(round(result["MAE"], 4)))
        self.lineEdit_MSE_LR.setText(str(round(result["MSE"], 4)))
        self.lineEdit_RMSE_LR.setText(str(round(result["RMSE"], 4)))
        self.lineEdit_ROC_LR.setText(str(round(result["ROC_SCORE"], 4)))

        # Hiển thị thông báo huấn luyện thành công
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Info")
        dlg.setIcon(QMessageBox.Icon.Information)
        dlg.setText(f"Train and evaluate {selected_model} model successful!")
        dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
        dlg.exec()

    def processTrainModel_and_Evaluate_DT(self):
        # Lấy lựa chọn từ comboBox
        selected_model = self.comboBox_LoadModel_DT.currentText()

        # Lấy dữ liệu từ giao diện người dùng
        test_size_dt = float(self.lineEdit_TestSize_DT.text()) / 100
        random_state_dt = int(self.lineEdit_RandomState_DT.text())

        # Khởi tạo mô hình phù hợp
        if selected_model == "With Oversampling":
            self.DecisionTreeModel = DecisionTreeModelOversampling(random_state_dt=random_state_dt)
        else:
            self.DecisionTreeModel = DecisionTreeModel(random_state_dt=random_state_dt)

        # Gọi prepare_data để tạo tập train/test theo test_size_lr
        self.DecisionTreeModel.prepare_data(test_size=test_size_dt)

        # Huấn luyện mô hình
        self.DecisionTreeModel.train()

        # Đánh giá mô hình
        result = self.DecisionTreeModel.evaluate()

        # Hiển thị kết quả trên giao diện
        self.lineEdit_MAE_DT.setText(str(round(result["MAE"], 4)))
        self.lineEdit_MSE_DT.setText(str(round(result["MSE"], 4)))
        self.lineEdit_RMSE_DT.setText(str(round(result["RMSE"], 4)))
        self.lineEdit_ROC_DT.setText(str(round(result["ROC_SCORE"], 4)))

        # Hiển thị thông báo huấn luyện thành công
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Info")
        dlg.setIcon(QMessageBox.Icon.Information)
        dlg.setText(f"Train and evaluate {selected_model} model successful!")
        dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
        dlg.exec()

    def processTrainModel_and_Evaluate_RF(self):
        # Lấy lựa chọn từ comboBox
        selected_model = self.comboBox_LoadModel_RF.currentText()

        # Lấy dữ liệu từ giao diện người dùng
        test_size_rf = float(self.lineEdit_TestSize_RF.text()) / 100
        estimators_rf = float(self.lineEdit_NEstimators_RF.text())
        random_state_rf = int(self.lineEdit_RandomState_RF.text())

        # Khởi tạo mô hình phù hợp
        if selected_model == "With Oversampling":
            self.RandomForestModel = RandomForestModelOversampling(random_state_rf=random_state_rf, N=estimators_rf)
        else:
            self.RandomForestModel = RandomForestModel(random_state_rf=random_state_rf, N=estimators_rf)

        # Gọi prepare_data để tạo tập train/test theo test_size_lr
        self.RandomForestModel.prepare_data(test_size=test_size_rf)

        # Huấn luyện mô hình
        self.RandomForestModel.train()

        # Đánh giá mô hình
        result = self.RandomForestModel.evaluate()

        # Hiển thị kết quả trên giao diện
        self.lineEdit_MAE_RF.setText(str(round(result["MAE"], 4)))
        self.lineEdit_MSE_RF.setText(str(round(result["MSE"], 4)))
        self.lineEdit_RMSE_RF.setText(str(round(result["RMSE"], 4)))
        self.lineEdit_ROC_RF.setText(str(round(result["ROC_SCORE"], 4)))

        # Hiển thị thông báo huấn luyện thành công
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Info")
        dlg.setIcon(QMessageBox.Icon.Information)
        dlg.setText(f"Train and evaluate {selected_model} model successful!")
        dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
        dlg.exec()

    def processTrainModel_and_Evaluate_XG(self):
        # Lấy lựa chọn từ comboBox
        selected_model = self.comboBox_LoadModel_XGBoost.currentText()

        # Lấy dữ liệu từ giao diện người dùng
        test_size_XG = float(self.lineEdit_TestSize_XGBoost.text()) / 100
        estimators_XG = float(self.lineEdit_NEstimators_XGBoost.text())
        random_state_XG = int(self.lineEdit_RandomState_XGBoost.text())

        # Khởi tạo mô hình phù hợp
        if selected_model == "With Oversampling":
            self.XGBoostModel = XGBoostModelOversampling(random_state_XG=random_state_XG, N=estimators_XG)
        else:
            self.XGBoostModel = XGBoostModel(random_state_XG=random_state_XG, N=estimators_XG)

        # Gọi prepare_data để tạo tập train/test theo test_size_lr
        self.XGBoostModel.prepare_data(test_size=test_size_XG)

        # Huấn luyện mô hình
        self.XGBoostModel.train()

        # Đánh giá mô hình
        result = self.XGBoostModel.evaluate()

        # Hiển thị kết quả trên giao diện
        self.lineEdit_MAE_XGBoost.setText(str(round(result["MAE"], 4)))
        self.lineEdit_MSE_XGBoost.setText(str(round(result["MSE"], 4)))
        self.lineEdit_RMSE_XGBoost.setText(str(round(result["RMSE"], 4)))
        self.lineEdit_ROC_XGBoost.setText(str(round(result["ROC_SCORE"], 4)))

        # Hiển thị thông báo huấn luyện thành công
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Info")
        dlg.setIcon(QMessageBox.Icon.Information)
        dlg.setText(f"Train and evaluate {selected_model} model successful!")
        dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
        dlg.exec()

    def processPickSavePath(self):
        filters = "trained model file (*.zip);;All files(*)"
        filename, selected_filter = QFileDialog.getSaveFileName(
            self.QMainWindow,
            filter=filters,
        )
        self.lineEdit_SaveModel_LR.setText(filename)
        self.lineEdit_SaveModel_DT.setText(filename)
        self.lineEdit_SaveModel_RF.setText(filename)
        self.lineEdit_SaveModel_XGBoost.setText(filename)

    def processSaveTrainedModel(self):
        trainedModelPath = self.lineEdit_SaveModel_LR.text()

        if trainedModelPath == "":
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn đường dẫn lưu trước khi lưu mô hình!")
            return

        # Danh sách model có thể lưu
        models = {
            "LogisticRegressionModelOversampling": self.LogisticRegressionModelOversampling,
            "DecisionTreeModelOversampling": self.DecisionTreeModelOversampling,
            "RandomForestModelOversampling": self.RandomForestModelOversampling,
            "XGBoostModelOversampling": self.XGBoostModelOversampling,
            "LogisticRegressionModel": self.LogisticRegressionModel,
            "DecisionTreeModel": self.DecisionTreeModel,
            "RandomForestModel": self.RandomForestModel,
            "XGBoostModel": self.XGBoostModel,
        }

        # Chỉ lọc các model đã train
        trained_models = {name: model for name, model in models.items() if model.trained_model is not None}

        # Nếu không có model nào được train, báo lỗi và dừng
        if not trained_models:
            QMessageBox.warning(self, "Lỗi", "Không có mô hình nào được train! Vui lòng train trước khi lưu.")
            return

        # Lưu các model đã train
        saved_models = []
        for model_name, model in trained_models.items():
            model.saveModel(f"{trainedModelPath}")
            saved_models.append(model_name)

        # Thông báo chỉ khi có ít nhất một model đã lưu
        QMessageBox.information(
            self,
            "Thành công",
            f"Đã lưu các mô hình: {', '.join(saved_models)}!"
        )

    def processPrediction_DT(self):
        try:
            # Mã hóa giá trị categorical
            gender_mapping = {"Male": 0, "Female": 1}
            vehicle_age_mapping = {"< 1 Year": 0, "1-2 Year": 1, "> 2 Years": 2}
            vehicle_damage_mapping = {"Yes": 1, "No": 0}

            # Lấy dữ liệu từ giao diện và loại bỏ khoảng trắng
            data_fields = {
                "Giới tính": self.lineEdit_Gender_DT.text().strip(),
                "Tuổi": self.lineEdit_Age_DT.text().strip(),
                "Bằng lái xe": self.lineEdit_DrivingLicense_DT.text().strip(),
                "Mã vùng": self.lineEdit_RegionCode_DT.text().strip(),
                "Bảo hiểm trước đó": self.lineEdit_PreviouslyInsured_DT.text().strip(),
                "Tuổi xe": self.lineEdit_VehicleAge_DT.text().strip(),
                "Thiệt hại xe": self.lineEdit_VehicleDamege_DT.text().strip(),
                "Phí bảo hiểm hàng năm": self.lineEdit_AnnualPremiun_DT.text().strip(),
                "Kênh bán hàng": self.lineEdit_PolicySalesChannel_DT.text().strip(),
                "Thời gian sử dụng": self.lineEdit_Vintage_DT.text().strip(),
                "Phí bảo hiểm điều chỉnh": self.lineEdit_AnnualPremiumAdjusted_DT.text().strip()
            }

            # Kiểm tra dữ liệu rỗng
            for field_name, value in data_fields.items():
                if not value:
                    QMessageBox.warning(self, "Lỗi", f"Trường '{field_name}' không được để trống! Vui lòng nhập dữ liệu.")
                    return

            # Chuyển đổi kiểu số
            try:
                age_DT = int(data_fields["Tuổi"])
                previously_insured_DT = int(data_fields["Bảo hiểm trước đó"])
                annual_premium_DT = int(data_fields["Phí bảo hiểm hàng năm"])
                annual_premium_adjusted_DT = int(data_fields["Phí bảo hiểm điều chỉnh"])
                region_code_DT = int(data_fields["Mã vùng"])
                policy_sales_channel_DT = int(data_fields["Kênh bán hàng"])
                vintage_DT = int(data_fields["Thời gian sử dụng"])
            except ValueError as e:
                QMessageBox.warning(self, "Lỗi", f"Dữ liệu nhập sai kiểu số: {e}")
                return

            # Mã hóa categorical
            gender_DT = gender_mapping.get(data_fields["Giới tính"])
            vehicle_age_DT = vehicle_age_mapping.get(data_fields["Tuổi xe"])
            vehicle_damage_DT = vehicle_damage_mapping.get(data_fields["Thiệt hại xe"])

            if gender_DT is None or vehicle_age_DT is None or vehicle_damage_DT is None:
                QMessageBox.warning(self, "Lỗi", "Một số trường nhập sai giá trị! Kiểm tra lại.")
                return

            # Chuyển đổi thành numpy array để tránh lỗi dtype='numeric'
            input_data = np.array([[
                gender_DT, age_DT, data_fields["Bằng lái xe"], region_code_DT,
                previously_insured_DT, vehicle_age_DT, vehicle_damage_DT,
                annual_premium_DT, policy_sales_channel_DT, vintage_DT,
                annual_premium_adjusted_DT
            ]], dtype=np.float64)  # Chuyển tất cả về số thực

            # Kiểm tra model trước khi dự đoán
            if self.DecisionTreeModel.trained_model is None:
                QMessageBox.warning(self, "Lỗi", "Mô hình chưa được train! Vui lòng train trước khi dự đoán.")
                return

            # Kiểm tra mô hình có tồn tại không
            if not hasattr(self.DecisionTreeModel, 'model'):
                QMessageBox.warning(self, "Lỗi", "Mô hình DecisionTree chưa được khởi tạo.")
                return

            # Kiểm tra lỗi khi predict
            try:
                response_dt = self.DecisionTreeModel.model.predict(input_data)
            except Exception as e:
                QMessageBox.warning(self, "Lỗi", f"Lỗi khi dự đoán: {e}")
                return

            # Hiển thị kết quả dự đoán lên giao diện
            self.lineEdit_Response_DT.setText(str(response_dt[0]))

        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi không xác định: {e}")

    def processPrediction_LR(self):
        try:
            # Mã hóa giá trị categorical
            gender_mapping = {"Male": 0, "Female": 1}
            vehicle_age_mapping = {"< 1 Year": 0, "1-2 Year": 1, "> 2 Years": 2}
            vehicle_damage_mapping = {"Yes": 1, "No": 0}

            # Lấy dữ liệu từ giao diện và loại bỏ khoảng trắng
            data_fields = {
                "Giới tính": self.lineEdit_Gender_LR.text().strip(),
                "Tuổi": self.lineEdit_Age_LR.text().strip(),
                "Bằng lái xe": self.lineEdit_DrivingLicense_LR.text().strip(),
                "Mã vùng": self.lineEdit_RegionCode_LR.text().strip(),
                "Bảo hiểm trước đó": self.lineEdit_PreviouslyInsured_LR.text().strip(),
                "Tuổi xe": self.lineEdit_VehicleAge_LR.text().strip(),
                "Thiệt hại xe": self.lineEdit_VehicleDamege_LR.text().strip(),
                "Phí bảo hiểm hàng năm": self.lineEdit_AnnualPremiun_LR.text().strip(),
                "Kênh bán hàng": self.lineEdit_PolicySalesChannel_LR.text().strip(),
                "Thời gian sử dụng": self.lineEdit_Vintage_LR.text().strip(),
                "Phí bảo hiểm điều chỉnh": self.lineEdit_AnnualPremiumAdjusted_LR.text().strip()
            }

            # Kiểm tra dữ liệu rỗng
            for field_name, value in data_fields.items():
                if not value:
                    QMessageBox.warning(self, "Lỗi", f"Trường '{field_name}' không được để trống! Vui lòng nhập dữ liệu.")
                    return

            # Chuyển đổi kiểu số
            try:
                age_LR = int(data_fields["Tuổi"])
                previously_insured_LR = int(data_fields["Bảo hiểm trước đó"])
                annual_premium_LR = int(data_fields["Phí bảo hiểm hàng năm"])
                annual_premium_adjusted_LR = int(data_fields["Phí bảo hiểm điều chỉnh"])
                region_code_LR = int(data_fields["Mã vùng"])
                policy_sales_channel_LR = int(data_fields["Kênh bán hàng"])
                vintage_LR = int(data_fields["Thời gian sử dụng"])
            except ValueError as e:
                QMessageBox.warning(self, "Lỗi", f"Dữ liệu nhập sai kiểu số: {e}")
                return

            # Mã hóa categorical
            gender_LR = gender_mapping.get(data_fields["Giới tính"])
            vehicle_age_LR = vehicle_age_mapping.get(data_fields["Tuổi xe"])
            vehicle_damage_LR = vehicle_damage_mapping.get(data_fields["Thiệt hại xe"])

            if gender_LR is None or vehicle_age_LR is None or vehicle_damage_LR is None:
                QMessageBox.warning(self, "Lỗi", "Một số trường nhập sai giá trị! Kiểm tra lại.")
                return

            # Chuyển đổi thành numpy array để tránh lỗi dtype='numeric'
            input_data = np.array([[
                gender_LR, age_LR, data_fields["Bằng lái xe"], region_code_LR,
                previously_insured_LR, vehicle_age_LR, vehicle_damage_LR,
                annual_premium_LR, policy_sales_channel_LR, vintage_LR,
                annual_premium_adjusted_LR
            ]], dtype=np.float64)  # ⚠ Chuyển tất cả về số thực

            # Kiểm tra model trước khi dự đoán
            if self.LogisticRegressionModel.trained_model is None:
                QMessageBox.warning(self, "Lỗi", "Mô hình chưa được train! Vui lòng train trước khi dự đoán.")
                return

            # Kiểm tra mô hình có tồn tại không
            if not hasattr(self.LogisticRegressionModel, 'model'):
                QMessageBox.warning(self, "Lỗi", "Mô hình LogisticRegression chưa được khởi tạo.")
                return

            # Kiểm tra lỗi khi predict
            try:
                response_lr = self.LogisticRegressionModel.model.predict(input_data)
            except Exception as e:
                QMessageBox.warning(self, "Lỗi", f"Lỗi khi dự đoán: {e}")
                return

            # Hiển thị kết quả dự đoán lên giao diện
            self.lineEdit_Response_LR.setText(str(response_lr[0]))

        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi không xác định: {e}")

    def processPrediction_RF(self):
        try:
            # Mã hóa giá trị categorical
            gender_mapping = {"Male": 0, "Female": 1}
            vehicle_age_mapping = {"< 1 Year": 0, "1-2 Year": 1, "> 2 Years": 2}
            vehicle_damage_mapping = {"Yes": 1, "No": 0}

            # Lấy dữ liệu từ giao diện và loại bỏ khoảng trắng
            data_fields = {
                "Giới tính": self.lineEdit_Gender_RF.text().strip(),
                "Tuổi": self.lineEdit_Age_RF.text().strip(),
                "Bằng lái xe": self.lineEdit_DrivingLicense_RF.text().strip(),
                "Mã vùng": self.lineEdit_RegionCode_RF.text().strip(),
                "Bảo hiểm trước đó": self.lineEdit_PreviouslyInsured_RF.text().strip(),
                "Tuổi xe": self.lineEdit_VehicleAge_RF.text().strip(),
                "Thiệt hại xe": self.lineEdit_VehicleDamege_RF.text().strip(),
                "Phí bảo hiểm hàng năm": self.lineEdit_AnnualPremiun_RF.text().strip(),
                "Kênh bán hàng": self.lineEdit_PolicySalesChannel_RF.text().strip(),
                "Thời gian sử dụng": self.lineEdit_Vintage_RF.text().strip(),
                "Phí bảo hiểm điều chỉnh": self.lineEdit_AnnualPremiumAdjusted_RF.text().strip()
            }

            # Kiểm tra dữ liệu rỗng
            for field_name, value in data_fields.items():
                if not value:
                    QMessageBox.warning(self, "Lỗi",
                                        f"Trường '{field_name}' không được để trống! Vui lòng nhập dữ liệu.")
                    return

            # Chuyển đổi kiểu số
            try:
                age_RF = int(data_fields["Tuổi"])
                previously_insured_RF = int(data_fields["Bảo hiểm trước đó"])
                annual_premium_RF = int(data_fields["Phí bảo hiểm hàng năm"])
                annual_premium_adjusted_RF = int(data_fields["Phí bảo hiểm điều chỉnh"])
                region_code_RF = int(data_fields["Mã vùng"])
                policy_sales_channel_RF = int(data_fields["Kênh bán hàng"])
                vintage_RF = int(data_fields["Thời gian sử dụng"])
            except ValueError as e:
                QMessageBox.warning(self, "Lỗi", f"Dữ liệu nhập sai kiểu số: {e}")
                return

            # Mã hóa categorical
            gender_RF = gender_mapping.get(data_fields["Giới tính"])
            vehicle_age_RF = vehicle_age_mapping.get(data_fields["Tuổi xe"])
            vehicle_damage_RF = vehicle_damage_mapping.get(data_fields["Thiệt hại xe"])

            if gender_RF is None or vehicle_age_RF is None or vehicle_damage_RF is None:
                QMessageBox.warning(self, "Lỗi", "Một số trường nhập sai giá trị! Kiểm tra lại.")
                return

            # Chuyển đổi thành numpy array để tránh lỗi dtype='numeric'
            input_data = np.array([[
                gender_RF, age_RF, data_fields["Bằng lái xe"], region_code_RF,
                previously_insured_RF, vehicle_age_RF, vehicle_damage_RF,
                annual_premium_RF, policy_sales_channel_RF, vintage_RF,
                annual_premium_adjusted_RF
            ]], dtype=np.float64)  # Chuyển tất cả về số thực

            # Kiểm tra model trước khi dự đoán
            if self.RandomForestModel.trained_model is None:
                QMessageBox.warning(self, "Lỗi", "Mô hình chưa được train! Vui lòng train trước khi dự đoán.")
                return

            # Kiểm tra mô hình có tồn tại không
            if not hasattr(self.RandomForestModel, 'model'):
                QMessageBox.warning(self, "Lỗi", "Mô hình RandomForest chưa được khởi tạo.")
                return

            # Kiểm tra lỗi khi predict
            try:
                response_rf = self.RandomForestModel.model.predict(input_data)
            except Exception as e:
                QMessageBox.warning(self, "Lỗi", f"Lỗi khi dự đoán: {e}")
                return

            # Hiển thị kết quả dự đoán lên giao diện
            self.lineEdit_Response_RF.setText(str(response_rf[0]))

        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi không xác định: {e}")

    def processPrediction_XG(self):
        try:
            # Mã hóa giá trị categorical
            gender_mapping = {"Male": 0, "Female": 1}
            vehicle_age_mapping = {"< 1 Year": 0, "1-2 Year": 1, "> 2 Years": 2}
            vehicle_damage_mapping = {"Yes": 1, "No": 0}

            # Lấy dữ liệu từ giao diện và loại bỏ khoảng trắng
            data_fields = {
                "Giới tính": self.lineEdit_Gender_XGBoost.text().strip(),
                "Tuổi": self.lineEdit_Age_XGBoost.text().strip(),
                "Bằng lái xe": self.lineEdit_DrivingLicense_XGBoost.text().strip(),
                "Mã vùng": self.lineEdit_RegionCode_XGBoost.text().strip(),
                "Bảo hiểm trước đó": self.lineEdit_PreviouslyInsured_XGBoost.text().strip(),
                "Tuổi xe": self.lineEdit_VehicleAge_XGBoost.text().strip(),
                "Thiệt hại xe": self.lineEdit_VehicleDamege_XGBoost.text().strip(),
                "Phí bảo hiểm hàng năm": self.lineEdit_AnnualPremiun_XGBoost.text().strip(),
                "Kênh bán hàng": self.lineEdit_PolicySalesChannel_XGBoost.text().strip(),
                "Thời gian sử dụng": self.lineEdit_Vintage_XGBoost.text().strip(),
                "Phí bảo hiểm điều chỉnh": self.lineEdit_AnnualPremiumAdjusted_XGBoost.text().strip()
            }

            # Kiểm tra dữ liệu rỗng
            for field_name, value in data_fields.items():
                if not value:
                    QMessageBox.warning(self, "Lỗi",
                                        f"Trường '{field_name}' không được để trống! Vui lòng nhập dữ liệu.")
                    return

            # Chuyển đổi kiểu số
            try:
                age_XG = int(data_fields["Tuổi"])
                previously_insured_XG = int(data_fields["Bảo hiểm trước đó"])
                annual_premium_XG = int(data_fields["Phí bảo hiểm hàng năm"])
                annual_premium_adjusted_XG = int(data_fields["Phí bảo hiểm điều chỉnh"])
                region_code_XG = int(data_fields["Mã vùng"])
                policy_sales_channel_XG = int(data_fields["Kênh bán hàng"])
                vintage_XG = int(data_fields["Thời gian sử dụng"])
            except ValueError as e:
                QMessageBox.warning(self, "Lỗi", f"Dữ liệu nhập sai kiểu số: {e}")
                return

            # Mã hóa categorical
            gender_XG = gender_mapping.get(data_fields["Giới tính"])
            vehicle_age_XG = vehicle_age_mapping.get(data_fields["Tuổi xe"])
            vehicle_damage_XG = vehicle_damage_mapping.get(data_fields["Thiệt hại xe"])

            if gender_XG is None or vehicle_age_XG is None or vehicle_damage_XG is None:
                QMessageBox.warning(self, "Lỗi", "Một số trường nhập sai giá trị! Kiểm tra lại.")
                return

            # Chuyển đổi thành numpy array để tránh lỗi dtype='numeric'
            input_data = np.array([[
                gender_XG, age_XG, data_fields["Bằng lái xe"], region_code_XG,
                previously_insured_XG, vehicle_age_XG, vehicle_damage_XG,
                annual_premium_XG, policy_sales_channel_XG, vintage_XG,
                annual_premium_adjusted_XG
            ]], dtype=np.float64)  # Chuyển tất cả về số thực

            # Kiểm tra model trước khi dự đoán
            if self.XGBoostModel.trained_model is None:
                QMessageBox.warning(self, "Lỗi", "Mô hình chưa được train! Vui lòng train trước khi dự đoán.")
                return

            # Kiểm tra mô hình có tồn tại không
            if not hasattr(self.XGBoostModel, 'model'):
                QMessageBox.warning(self, "Lỗi", "Mô hình XGBoost chưa được khởi tạo.")
                return

            # Kiểm tra lỗi khi predict
            try:
                response_xg = self.XGBoostModel.model.predict(input_data)
            except Exception as e:
                QMessageBox.warning(self, "Lỗi", f"Lỗi khi dự đoán: {e}")
                return

            # Hiển thị kết quả dự đoán lên giao diện
            self.lineEdit_Response_XGBoost.setText(str(response_xg[0]))

        except Exception as e:
            QMessageBox.warning(self, "Lỗi", f"Lỗi không xác định: {e}")

    def showWindow(self):
        self.showWindow()

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