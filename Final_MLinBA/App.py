from PyQt6.QtWidgets import QApplication, QMainWindow

from MLinBA.Final_MLinBA.UI.LoginWindowExt import LoginWindowExt

qApp=QApplication([])
QMainWindow=QMainWindow()
window=LoginWindowExt()
window.setupUi(QMainWindow)
window.showWindow()
qApp.exec()