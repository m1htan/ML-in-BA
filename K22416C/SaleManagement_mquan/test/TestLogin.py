from PyQt6.QtWidgets import QApplication, QMainWindow

from K22416C.SaleManagement_mquan.ui.LoginMainWindowExt import LoginMainWindowExt

app=QApplication([])
mainwindow = QMainWindow()
myui = LoginMainWindowExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()

