import sys

from SalesManagement.UI.MainProgramMainWindow import Ui_MainWindow

class MainProgramMainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
    def showWindow(self):
        self.MainWindow.show()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.actionthoatphanmem.triggered.connect(self.xuly_thoat)

    def xuly_thoat(self):
        sys.exit(0)