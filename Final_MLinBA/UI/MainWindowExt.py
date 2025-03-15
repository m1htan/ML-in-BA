import numpy as np
import pandas as pd
from PyQt6.uic.properties import QtWidgets
from matplotlib import pyplot as plt
from matplotlib.backends.backend_template import FigureCanvas

from MLinBA.Final_MLinBA.Model.ML.WithOversampling.DecisionTree import DecisionTreeModelOversampling
from MLinBA.Final_MLinBA.Model.ML.WithOversampling.LogisticRegression import LogisticRegressionModelOversampling
from MLinBA.Final_MLinBA.Model.ML.WithOversampling.RandomForest import RandomForestModelOversampling
from MLinBA.Final_MLinBA.Model.ML.WithOversampling.XGBoost import XGBoostModelOversampling

from MLinBA.Final_MLinBA.Model.ML.WithoutOversampling.DecisionTree import DecisionTreeModel
from MLinBA.Final_MLinBA.Model.ML.WithoutOversampling.LogisticRegression import LogisticRegressionModel
from MLinBA.Final_MLinBA.Model.ML.WithoutOversampling.RandomForest import RandomForestModel
from MLinBA.Final_MLinBA.Model.ML.WithoutOversampling.XGBoost import XGBoostModel

from MLinBA.Final_MLinBA.Model.Prepare.PrepareData import df
from MLinBA.Final_MLinBA.UI.LoginWindowExt import LoginWindowExt
from MLinBA.Final_MLinBA.UI.MainWindow import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QTableWidgetItem, QApplication


class MainWindowExt(QMainWindow, Ui_MainWindow):
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
        #self.pushButtonPredict_RF.clicked.connect(self.processPrediction_RF)
        #self.pushButtonPredict_XGBoost.clicked.connect(self.processPrediction_XG)

    def initUI(self):
        # Kết nối các nút với hàm xử lý sự kiện
        self.actionConnect_Database.triggered.connect(self.openDatabaseConnectUI)
        self.actionExit.triggered.connect(self.processExit)

        self.checkEnableWidget(False)

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
        pass

    def MaleFemaleRatio(self):
        pass

    def AverageCustomerAge(self):
        pass

    def CusWithLicense(self):
        pass

    def InsuaranceBuyers(self):
        pass

    def DistributionOfVehicleAge(self):
        pass

    def CusWithVehicleDamage(self):
        pass

    def ApprovalRate(self):
        pass

    def TopCusRegions(self):
        pass

    def TopResponsiveRegions(self):
        pass

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

    def openDatabaseConnectUI(self):
        self.dbwindow = QMainWindow()
        self.LoginWindowExt.setupUi(self.dbwindow)
        self.dbwindow.show()

    def showDataIntoTableWidget(self,df):
        self.tableWidget_ListOfData.setRowCount(0)
        self.tableWidget_ListOfData.setColumnCount(len(df.columns))
        for i in range(len(df.columns)):
            columnHeader = df.columns[i]
            self.tableWidget_ListOfData.setHorizontalHeaderItem(i, QTableWidgetItem(columnHeader))
        row = 0
        for item in df.iloc:
            arr = item.values.tolist()
            self.tableWidget_ListOfData.insertRow(row)
            j=0
            for data in arr:
                self.tableWidget_ListOfData.setItem(row, j, QTableWidgetItem(str(data)))
                j=j+1
            row = row + 1

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

    def checkEnableWidget(self,flag=True):
        self.pushButtonTotalNumberOfCustomer.setEnabled(flag)
        self.pushButtonMaleFemaleRatio.setEnabled(flag)
        self.pushButtonAverageCustomerAge.setEnabled(flag)
        self.pushButtonCusWithLicense.setEnabled(flag)
        self.pushButtonInsuaranceBuyers.setEnabled(flag)

        self.pushButtonDistributionOfVehicleAge.setEnabled(flag)
        self.pushButtonCusWithVehicleDamage.setEnabled(flag)
        self.pushButtonApprovalRate.setEnabled(flag)

        self.pushButtonTopCusRegions.setEnabled(flag)
        self.pushButtonTopResponsiveRegions.setEnabled(flag)

    def processPrediction_DT(self):
        try:
            gender_DT = self.lineEdit_Gender_DT.text()
            age_DT = int(self.lineEdit_Age_DT.text())
            driving_license_DT = self.lineEdit_DrivingLicense_DT.text()
            region_code_DT = self.lineEdit_RegionCode_DT.text()
            previously_insured_DT = int(self.lineEdit_PreviouslyInsured_DT.text())
            vehicle_age_DT = self.lineEdit_VehicleAge_DT.text()
            vehicle_damage_DT = self.lineEdit_VehicleDamege_DT.text()
            annual_premium_DT = int(self.lineEdit_AnnualPremiun_DT.text())
            policy_sales_channel_DT = self.lineEdit_PolicySalesChannel_DT.text()
            vintage_DT = self.lineEdit_Vintage_DT.text()
            annual_premium_adjusted_DT = int(self.lineEdit_AnnualPremiumAdjusted_DT.text())

            if not all([gender_DT, age_DT, driving_license_DT, region_code_DT, previously_insured_DT,
                        vehicle_age_DT, vehicle_damage_DT, annual_premium_DT, policy_sales_channel_DT,
                        vintage_DT, annual_premium_adjusted_DT]):
                QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin trước khi dự đoán!")
                return

            input_data = [[
                gender_DT, age_DT, driving_license_DT, region_code_DT,
                previously_insured_DT, vehicle_age_DT, vehicle_damage_DT,
                annual_premium_DT, policy_sales_channel_DT, vintage_DT, annual_premium_adjusted_DT
            ]]

            response_dt = self.DecisionTreeModel.model.predict(input_data)

            self.lineEdit_Response_DT.setText(str(response_dt[0]))

        except ValueError:
            QMessageBox.warning(self, "Lỗi", "Dữ liệu đầu vào không hợp lệ! Vui lòng kiểm tra lại.")

    def processPrediction_LR(self):
        try:
            # 🔥 Mã hóa giá trị categorical
            gender_mapping = {"Male": 0, "Female": 1}
            vehicle_age_mapping = {"< 1 Year": 0, "1-2 Year": 1, "> 2 Years": 2}
            vehicle_damage_mapping = {"Yes": 1, "No": 0}

            # 🛠 Lấy dữ liệu từ giao diện và loại bỏ khoảng trắng
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

            # ✅ Kiểm tra dữ liệu rỗng
            for field_name, value in data_fields.items():
                if not value:
                    QMessageBox.warning(self, "Lỗi", f"Trường '{field_name}' không được để trống! Vui lòng nhập dữ liệu.")
                    return

            # ✅ Chuyển đổi kiểu số
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

            # ✅ Mã hóa categorical
            gender_LR = gender_mapping.get(data_fields["Giới tính"])
            vehicle_age_LR = vehicle_age_mapping.get(data_fields["Tuổi xe"])
            vehicle_damage_LR = vehicle_damage_mapping.get(data_fields["Thiệt hại xe"])

            if gender_LR is None or vehicle_age_LR is None or vehicle_damage_LR is None:
                QMessageBox.warning(self, "Lỗi", "Một số trường nhập sai giá trị! Kiểm tra lại.")
                return

            # 🔥 Chuyển đổi thành numpy array để tránh lỗi dtype='numeric'
            input_data = np.array([[
                gender_LR, age_LR, data_fields["Bằng lái xe"], region_code_LR,
                previously_insured_LR, vehicle_age_LR, vehicle_damage_LR,
                annual_premium_LR, policy_sales_channel_LR, vintage_LR,
                annual_premium_adjusted_LR
            ]], dtype=np.float64)  # ⚠ Chuyển tất cả về số thực

            # 🛠 Kiểm tra model trước khi dự đoán
            if self.LogisticRegressionModel.trained_model is None:
                QMessageBox.warning(self, "Lỗi", "Mô hình chưa được train! Vui lòng train trước khi dự đoán.")
                return

            # 🔥 Kiểm tra mô hình có tồn tại không
            if not hasattr(self.LogisticRegressionModel, 'model'):
                QMessageBox.warning(self, "Lỗi", "Mô hình LogisticRegression chưa được khởi tạo.")
                return

            # 🛠 Kiểm tra lỗi khi predict
            try:
                response_lr = self.LogisticRegressionModel.model.predict(input_data)
            except Exception as e:
                QMessageBox.warning(self, "Lỗi", f"Lỗi khi dự đoán: {e}")
                return

            # ✅ Hiển thị kết quả dự đoán lên giao diện
            self.lineEdit_Response_LR.setText(str(response_lr[0]))

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