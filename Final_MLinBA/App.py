from PyQt6.QtWidgets import QApplication, QMainWindow

from MLinBA.Final_MLinBA.UI.LoginWindowExt import LoginWindowExt

qApp=QApplication([])
qmainWindow=QMainWindow()
window=LoginWindowExt()
window.setupUi(qmainWindow)
window.show()
qApp.exec()