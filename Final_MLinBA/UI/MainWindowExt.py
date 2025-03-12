from MLinBA.Final_MLinBA.UI import MainWindow
from MLinBA.Final_MLinBA.UI.MainWindow import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow

class MainWindowExt(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.MainWindow=MainWindow

    def initUI(self):
        # Kết nối sự kiện với các button
        self.pushButtonCustomerAge.clicked.connect(self.on_customer_age_clicked)
        self.pushButtonAnnualPremium.clicked.connect(self.on_annual_premium_clicked)
        self.pushButtonByGenderAndVehicleDamage.clicked.connect(self.on_gender_vehicle_damage_clicked)
        self.pushButtonByAgeGroup.clicked.connect(self.on_age_group_clicked)
        self.pushButtonByVehicleAge.clicked.connect(self.on_vehicle_age_clicked)
        self.pushButton_LoadModel.clicked.connect(self.on_load_model_clicked)
        self.pushButton_TrainModel.clicked.connect(self.on_train_model_clicked)
        self.pushButtonPredict.clicked.connect(self.on_predict_clicked)
        self.pushButton_SaveModel.clicked.connect(self.on_save_model_clicked)

    def on_customer_age_clicked(self):
        print("Button 'Customer Age' clicked")

    def on_annual_premium_clicked(self):
        print("Button 'Annual Premium' clicked")

    def on_gender_vehicle_damage_clicked(self):
        print("Button 'By Gender and Vehicle Damage' clicked")

    def on_age_group_clicked(self):
        print("Button 'By Age Group' clicked")

    def on_vehicle_age_clicked(self):
        print("Button 'By Vehicle Age' clicked")

    def on_load_model_clicked(self):
        print("Loading model...")

    def on_train_model_clicked(self):
        print("Training model...")

    def on_predict_clicked(self):
        print("Predicting...")

    def on_save_model_clicked(self):
        print("Saving model...")

    def xuly_momanhinh_qlspdm(self):
        self.mainwindow = QMainWindow()
        self.myui = MainWindowExt()
        self.myui.setupUi(self.mainwindow)
        self.myui.showWindow()
