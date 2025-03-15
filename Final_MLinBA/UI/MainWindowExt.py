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
        self.LogisticRegression = LogisticRegressionModel()
        self.RandomForest = RandomForestModel()
        self.XGBoost = XGBoostModel()

    def setupUi(self, MainWindow):
        Ui_MainWindow.setupUi(self, MainWindow)

        self.pushButtonSavePath_LR.clicked.connect(self.processPickSavePath)

        self.pushButton_SaveModel_LR.clicked.connect(self.processSaveTrainedModel)
        self.pushButton_SaveModel_DT.clicked.connect(self.processSaveTrainedModel)
        self.pushButton_SaveModel_RF.clicked.connect(self.processSaveTrainedModel)
        self.pushButton_SaveModel_XGBoost.clicked.connect(self.processSaveTrainedModel)

        self.pushButton_TrainModel_LR.clicked.connect(self.processTrainModel_and_Evaluate_LR)
        self.pushButton_TrainModel_DT.clicked.connect(self.processTrainModel_and_Evaluate_DT)
        self.pushButton_TrainModel_RF.clicked.connect(self.processTrainModel_and_Evaluate_RF)
        self.pushButton_TrainModel_XGBoost.clicked.connect(self.processTrainModel_and_Evaluate_XG)

    def initUI(self):
        # Kết nối các nút với hàm xử lý sự kiện
        self.actionConnect_Database.triggered.connect(self.openDatabaseConnectUI)
        # self.actionExit.triggered.connect(self.processExit)

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
        test_size_dt = float(self.lineEdit_TestSize_LR.text()) / 100
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

    def processSaveTrainedModel(self):
        trainedModelPath=self.lineEdit_SaveModel_LR.text()
        if trainedModelPath=="":
            return

        ret=self.LogisticRegressionModelOversampling.saveModel(trainedModelPath)

        if self.LogisticRegressionModelOversampling.trained_model is None:
            QMessageBox.warning(self, "Lỗi", "Mô hình chưa được huấn luyện! Vui lòng train trước khi lưu.")
            return

        dlg = QMessageBox(self)
        dlg.setWindowTitle("Info")
        dlg.setIcon(QMessageBox.Icon.Information)
        dlg.setText(f"Saved Trained machine learning model successful at [{trainedModelPath}]!")
        buttons = QMessageBox.StandardButton.Yes
        dlg.setStandardButtons(buttons)
        buttons = dlg.exec()

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

    def processPrediction(self):
        gender = self.lineEditGender.text()
        age = int(self.lineEditAge.text())
        payment = self.lineEditPaymentMethod.text()
        if len(self.purchaseLinearRegression.trainedmodel.columns_input)==3:
            predicted_price = self.purchaseLinearRegression.predictPriceFromGenderAndAgeAndPayment(gender, age, payment)
        else:
            predicted_price = self.purchaseLinearRegression.predictPriceFromGenderAndAge(gender, age)
        self.lineEditPredictedPrice.setText(str(predicted_price[0]))

    def showWindow(self):
        self.showWindow()

    def processExit(self):
        # ✅ Hiển thị hộp thoại xác nhận
        reply = QMessageBox.question(
            self,
            "Xác nhận thoát",
            "Bạn có chắc chắn muốn thoát chương trình?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No  # Mặc định là "No"
        )

        # ✅ Nếu chọn "Yes", thoát chương trình
        if reply == QMessageBox.StandardButton.Yes:
            QApplication.quit()