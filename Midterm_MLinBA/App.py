from PyQt6.QtWidgets import QApplication, QMainWindow

from UI.LoginWindowExt import LoginWindowExt

app=QApplication([])
qmainWindow = QMainWindow()
myui = LoginWindowExt()
myui.show()
app.exec()