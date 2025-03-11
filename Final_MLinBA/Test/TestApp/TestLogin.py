from PyQt6.QtWidgets import QApplication, QMainWindow

from MLinBA.Final_MLinBA.UI.LoginWindowExt import LoginWindowExt

app=QApplication([])
qmainWindow = QMainWindow()
myui = LoginWindowExt()
myui.setupUi(qmainWindow)
myui.show()
app.exec()