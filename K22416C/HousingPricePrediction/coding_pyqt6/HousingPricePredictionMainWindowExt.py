from MLinBA.K22416C.HousingPricePrediction.coding_pyqt6.HousingPricePredictionMainWindow import Ui_MainWindow
import pickle
import os


class HousingPricePredictionMainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.SetupSignalandSlot()
        self.populate_comboBox()  # Gọi hàm điền combobox

    def showWindow(self):
        self.MainWindow.show()

    def SetupSignalandSlot(self):
        self.pushButtonPredict.clicked.connect(self.process_predict_housepricing)

    def process_predict_housepricing(self):
        AreaIncome=float(self.lineEditIncome.text())
        AreaHouseAge=float(self.lineEditAge.text())
        AreaNumberOfRooms=float(self.lineEditRooms.text())
        AreaNumberOfBedrooms=float(self.lineEditBedrooms.text())
        AreaPopulation=float(self.lineEditPopulation.text())


        modelname = "../TrainedModel/housingmodel.zip"

        if self.comboBoxTrainedModel.currentIndex()!=-1:
            modelname=f"../TrainedModel/{self.comboBoxTrainedModel.currentText()}"

        trainedmodel = pickle.load(open(modelname, 'rb'))
        prediction = trainedmodel.predict([[AreaIncome, AreaHouseAge, AreaNumberOfRooms, AreaNumberOfBedrooms, AreaPopulation]])
        print("kết quả =", prediction)
        self.lineEditPredict.setText(f'{prediction[0]}')

    def populate_comboBox(self):
        model_dir = "../TrainedModel"
        if os.path.exists(model_dir):  # Kiểm tra thư mục có tồn tại không
            models = sorted(set(f for f in os.listdir(model_dir) if f.endswith(".zip")))  # Loại bỏ trùng lặp và sắp xếp
            self.comboBoxTrainedModel.clear()  # Xóa danh sách cũ để tránh bị trùng lặp
            self.comboBoxTrainedModel.addItems(models)  # Thêm danh sách mới vào combobox

