from MLinBA.Final_MLinBA.UI.LoginWindowExt import LoginWindowExt
from MLinBA.Final_MLinBA.UI.MainWindow import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QTableWidgetItem
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.LoginWindowExt = LoginWindowExt()
        self.LoginWindowExt.parent = self
        self.chartHandle = ChartHandle()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.verticalLayout_ChartVisualization.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.setupPlot()

        self.actionConnect_Database.triggered.connect(self.openDatabaseConnectUI)
        self.actionSaved_trained_ML_model.triggered.connect(self.processSaveTrainedModel)
        self.actionLoad_trained_ML_model.triggered.connect(self.processLoadTrainedModel)
        self.actionExit.triggered.connect(self.MainWindow.close)

        self.pushButtonCustomerAge.clicked.connect(self.showCustomerAge)
        self.pushButtonAnnualPremium.clicked.connect(self.showAnnualPremium)
        self.pushButtonByGenderAndVehicleDamage.clicked.connect(self.showByGenderAndVehicleDamage)
        self.pushButtonByAgeGroup.clicked.connect(self.showByAgeGroup)
        self.pushButtonByVehicleAge.clicked.connect(self.showByVehicleAge)

        self.pushButton_LoadModel.clicked.connect(self.processLoadTrainedModel)
        self.pushButton_SaveModel.clicked.connect(self.processSaveTrainedModel)
        self.pushButton_TrainModel.clicked.connect(self.processTrainModel)
        self.pushButtonPredict.clicked.connect(self.processPrediction)

        self.checkEnableWidget(False)

    def show(self):
        self.MainWindow.show()

    def checkEnableWidget(self, flag=True):
        self.pushButtonCustomerAge.setEnabled(flag)
        self.pushButtonAnnualPremium.setEnabled(flag)
        self.pushButtonByGenderAndVehicleDamage.setEnabled(flag)
        self.pushButtonByAgeGroup.setEnabled(flag)
        self.pushButtonByVehicleAge.setEnabled(flag)

    def setupPlot(self):
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self.MainWindow)

        self.verticalLayout_ChartVisualization.addWidget(self.toolbar)
        self.verticalLayout_ChartVisualization.addWidget(self.canvas)

    def openDatabaseConnectUI(self):
        dbwindow = QMainWindow()
        self.databaseConnectEx.setupUi(dbwindow)
        self.databaseConnectEx.show()

    def showDataIntoTableWidget(self, df):
        self.tableWidget_ListOfData.setRowCount(0)
        self.tableWidget_ListOfData.setColumnCount(len(df.columns))
        for i in range(len(df.columns)):
            columnHeader = df.columns[i]
            self.tableWidget_ListOfData.setHorizontalHeaderItem(i, QTableWidgetItem(columnHeader))
        row = 0
        for item in df.iloc:
            arr = item.values.tolist()
            self.tableWidget_ListOfData.insertRow(row)
            j = 0
            for data in arr:
                self.tableWidget_ListOfData.setItem(row, j, QTableWidgetItem(str(data)))
                j += 1
            row += 1

    def showCustomerAge(self):
        df = self.purchaseLinearRegression.processCustomerAge()
        self.showDataIntoTableWidget(df)
        self.chartHandle.visualizeBarChart(self.figure, self.canvas, df, "age", "count", "Customer Age Distribution")

    def showAnnualPremium(self):
        df = self.purchaseLinearRegression.processAnnualPremium()
        self.showDataIntoTableWidget(df)
        self.chartHandle.visualizeBarChart(self.figure, self.canvas, df, "annual_premium", "count", "Annual Premium Distribution")

    def showByGenderAndVehicleDamage(self):
        df = self.purchaseLinearRegression.processGenderAndVehicleDamage()
        self.showDataIntoTableWidget(df)
        self.chartHandle.visualizeMultiBarChart(self.figure, self.canvas, df, "gender", "count", "vehicle_damage", "Gender and Vehicle Damage Distribution")

    def showByAgeGroup(self):
        df = self.purchaseLinearRegression.processAgeGroup()
        self.showDataIntoTableWidget(df)
        self.chartHandle.visualizeBarChart(self.figure, self.canvas, df, "age_group", "count", "Age Group Distribution")

    def showByVehicleAge(self):
        df = self.purchaseLinearRegression.processVehicleAge()
        self.showDataIntoTableWidget(df)
        self.chartHandle.visualizeBarChart(self.figure, self.canvas, df, "vehicle_age", "count", "Vehicle Age Distribution")

    def processTrainModel(self):
        test_size = float(self.lineEdit_TextSize.text()) / 100
        random_state = int(self.lineEdit_RandomState.text())
        self.purchaseLinearRegression.processTrain(test_size, random_state)
        QMessageBox.information(self.MainWindow, "Info", "Train machine learning model successful!")

    def processEvaluateTrainedModel(self):
        result = self.purchaseLinearRegression.evaluate()
        self.lineEdit_MAE.setText(str(result.MAE))
        self.lineEdit_MSE.setText(str(result.MSE))
        self.lineEdit_RMSE.setText(str(result.RMSE))
        self.lineEdit_RSquare.setText(str(result.R2_SCORE))
        self.lineEdit_ROC_AUC.setText(str(result.ROC_AUC))

    def processSaveTrainedModel(self):
        filters = "trained model file (*.zip);;All files(*)"
        filename, _ = QFileDialog.getSaveFileName(self.MainWindow, filter=filters)
        if filename:
            self.purchaseLinearRegression.saveModel(filename)
            QMessageBox.information(self.MainWindow, "Info", f"Saved Trained machine learning model successful at [{filename}]!")

    def processLoadTrainedModel(self):
        filters = "trained model file (*.zip);;All files(*)"
        filename, _ = QFileDialog.getOpenFileName(self.MainWindow, filter=filters)
        if filename:
            self.purchaseLinearRegression.loadModel(filename)
            QMessageBox.information(self.MainWindow, "Info", f"Load Trained machine learning model successful from [{filename}]!")

    def processPrediction(self):
        gender = self.lineEditGender.text()
        age = int(self.lineEditAge.text())
        payment_method = self.lineEditPaymentMethod.text()
        predicted_price = self.purchaseLinearRegression.predict(gender, age, payment_method)
        self.lineEditPredictedPrice.setText(str(predicted_price[0]))