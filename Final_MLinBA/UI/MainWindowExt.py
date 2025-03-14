import pandas as pd
from PyQt6.uic.properties import QtWidgets
from matplotlib import pyplot as plt
from matplotlib.backends.backend_template import FigureCanvas

from MLinBA.Final_MLinBA.Model.Prepare.PrepareData import X, y
from MLinBA.Final_MLinBA.UI.LoginWindowExt import LoginWindowExt
from MLinBA.Final_MLinBA.UI.MainWindow import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QFileDialog


class MainWindowExt(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.Ui_MainWindow = Ui_MainWindow()
        self.QMainWindow=QMainWindow()
        self.setupUi(self)
        self.initUI()
        self.LoginWindowExt=LoginWindowExt()
        self.LoginWindowExt.parent=self
        self.LogisticRegressionModel= self.LogisticRegressionModel()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.LoginWindowExt=LoginWindowExt

    def initUI(self):
        # Kết nối các nút với hàm xử lý sự kiện
        self.pushButtonCustomerAge.clicked.connect(self.show_customer_age)
        self.pushButtonAnnualPremium.clicked.connect(self.show_annual_premium)
        self.pushButtonByGenderAndVehicleDamage.clicked.connect(self.show_gender_vehicle_damage)
        self.pushButtonByAgeGroup.clicked.connect(self.show_age_group)
        self.pushButtonByVehicleAge.clicked.connect(self.show_vehicle_age)

        # Load dữ liệu ban đầu
        self.data = None
        self.model = None

    def show_customer_age(self):
        pass

    def show_annual_premium(self):
        pass

    def show_gender_vehicle_damage(self):
        pass

    def show_age_group(self):
        pass

    def show_vehicle_age(self):
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
        dbwindow = QMainWindow()
        self.LoginWindowExt.setupUi(dbwindow)
        self.LoginWindowExt.showWindow()

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

    def processTrainModel_LR(self):
        columns_input=X
        column_target=y

        test_size_lr=float(self.lineEdit_TextSize_LR.text())/100
        regularization_lr=int(self.lineEdit_C_LR.text())
        max_iter_lr=int(self.lineEdit_MaxIter_LR.text())

        self.LogisticRegressionModel = self.LogisticRegressionModel()
        self.LogisticRegressionModel.connector = self.LoginWindowExt.connector
        self.LogisticRegressionModel.processTrain(columns_input, column_target, test_size_lr, regularization_lr,max_iter_lr)

        dlg = QMessageBox(self.LoginWindowExt)
        dlg.setWindowTitle("Info")
        dlg.setIcon(QMessageBox.Icon.Information)
        dlg.setText("Train machine learning model successful!")
        buttons = QMessageBox.StandardButton.Yes
        dlg.setStandardButtons(buttons)
        button = dlg.exec()

    def processEvaluateTrainedModel_LR(self):
        result = self.LogisticRegressionModel.evaluate()
        self.lineEdit_MAE_LR.setText(str(result.MAE))
        self.lineEdit_MSE_LR.setText(str(result.MSE))
        self.lineEdit_RMSE_LR.setText(str(result.RMSE))
        self.lineEdit_ROC_LR.setText(str(result.ROC_SCORE))

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
        ret = self.LogisticRegressionModel.saveModel(trainedModelPath)
        dlg = QMessageBox(self.Ui_MainWindow)
        dlg.setWindowTitle("Info")
        dlg.setIcon(QMessageBox.Icon.Information)
        dlg.setText(f"Saved Trained machine learning model successful at [{trainedModelPath}]!")
        buttons = QMessageBox.StandardButton.Yes
        dlg.setStandardButtons(buttons)
        button = dlg.exec()

    def processLoadTrainedModel(self):
        # setup for QFileDialog
        filters = "trained model file (*.zip);;All files(*)"
        filename, selected_filter = QFileDialog.getOpenFileName(
            self.QMainWindow,
            filter=filters,
        )
        if filename=="":
            return
        self.pushButtonLoadPath_LR.set(filename)
        self.LogisticRegressionModel.loadModel(filename)
        dlg = QMessageBox(self.QMainWindow)
        dlg.setWindowTitle("Info")
        dlg.setIcon(QMessageBox.Icon.Information)
        dlg.setText(f"Load Trained machine learning model successful from [{filename}]!")
        buttons = QMessageBox.StandardButton.Yes
        dlg.setStandardButtons(buttons)
        button = dlg.exec()

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
        self.show()

    def LogisticRegressionModel(self):
        pass
