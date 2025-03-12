from PyQt6.QtWidgets import QApplication, QMainWindow

from MLinBA.Final_MLinBA.UI.LoginWindowExt import LoginWindowExt

app=QApplication([])
QMainWindow = QMainWindow()
myui = LoginWindowExt()
myui.setupUi(QMainWindow)
myui.showWindow()
app.exec()