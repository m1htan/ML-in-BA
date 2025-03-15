from PyQt6.QtWidgets import QApplication, QMainWindow

from K22416C.HousingPricePrediction.coding_pyqt6.HousingPricePredictionMainWindowExt import \
    HousingPricePredictionMainWindowExt

app=QApplication([])
mainwindow = QMainWindow()
myui = HousingPricePredictionMainWindowExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()