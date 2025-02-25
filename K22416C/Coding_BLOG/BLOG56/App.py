from PyQt6.QtWidgets import QApplication, QMainWindow

from K22416C.Coding_BLOG.BLOG56.UI.MainWindowEx import MainWindowEx

qApp=QApplication([])
qmainWindow=QMainWindow()
window=MainWindowEx()
window.setupUi(qmainWindow)
window.show()
qApp.exec()