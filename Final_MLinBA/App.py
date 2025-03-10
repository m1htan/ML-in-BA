from PyQt6.QtWidgets import QApplication, QMainWindow

from FinalProject.UI.ConnectionExt import ConnectionExt

qApp=QApplication([])
qmainWindow=QMainWindow()
window=ConnectionExt()
window.setupUi(qmainWindow)
window.show()
qApp.exec()