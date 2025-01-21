from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QWidget

from SalesManagement.UI.LoginMainWindow import Ui_MainWindow

class LoginMainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButton_2.clicked.connect(self.xuly_dangnhap)

    def xuly_dangnhap(self):
        username=self.lineidtusername.text()
        password=self.lineEditpassword.text()

        # Giả lập đăng nhập (Hôm sau truy vấn thật trong CSDL)

        if username=='admin' and password=='123':
            pass
        else:
            self.msg=QMessageBox()
            self.widget = QWidget()
            self.widget.setWindowTitle("Login thất bại")
            self.widget.setWindowTitle("Bạn đăng nhập thất bại.\nKiểm tra lại thông tin đăng nhập")
            self.msg.setIcon(QMessageBox.Icon.Critial)
            self.msg.show()




