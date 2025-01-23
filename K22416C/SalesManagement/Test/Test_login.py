from PyQt6.QtWidgets import QApplication, QMainWindow

from SalesManagement.UI.LoginMainWindowExt import LoginMainWindowExt

app=QApplication([])
mainwindow = QMainWindow()
myui = LoginMainWindowExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()