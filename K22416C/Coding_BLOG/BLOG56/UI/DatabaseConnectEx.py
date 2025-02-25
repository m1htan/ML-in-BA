import traceback

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox

from K22416C.Coding_BLOG.BLOG56.Connectors.Connector import Connector
from K22416C.Coding_BLOG.BLOG56.UI.DatabaseConnect import Ui_MainWindow


class DatabaseConnectEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.pushButtonConnect.clicked.connect(self.connectDatabase)
    def connectDatabase(self):
        try:
            self.connector=Connector()
            self.connector.server=self.lineEditServer.text()
            self.connector.port=(int)(self.lineEditPort.text())
            self.connector.database=self.lineEditDatabase.text()
            self.connector.username=self.lineEditUser.text()
            self.connector.password=self.lineEditPassword.text()
            self.connector.connect()
            self.msg=QMessageBox()
            self.msg.setText("Connect database successful!")
            self.msg.setWindowTitle("Info")
            #self.msg.show()
            self.MainWindow.close()
            if self.parent!=None:
                self.parent.checkEnableWidget(True)
        except:
            traceback.print_exc()
            self.msg = QMessageBox()
            self.msg.setText("Connect database failed")
            self.msg.setWindowTitle("Info")
            self.msg.show()
    def show(self):
        self.MainWindow.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.MainWindow.show()