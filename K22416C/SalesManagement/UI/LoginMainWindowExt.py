from PyQt6.QtWidgets import QMessageBox, QMainWindow

from K22416C.SalesManagement.UI.LoginMainWindow import Ui_MainWindow
from K22416C.SalesManagement.UI.MainProgramMainWindowExt import MainProgramMainWindowExt
from K22416C.SalesManagement.libs.nhanvienconnector import NhanVienConnector


class LoginMainWindowExt(Ui_MainWindow):
    def __init__(self):  # Sửa từ __int__ thành __init__
        super().__init__()
        self.nvconnector = NhanVienConnector()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButton.clicked.connect(self.xuly_dangnhap)

    def xuly_dangnhap(self):
        username=self.lineEdit.text()
        password=self.lineEdit_2.text()

        #giả lập đăng nhập (hôm sau truy vấn thật trong CSDL)
        #gọi kết nối cơ sở dữ liệu MySQL
        self.nvconnector.connect()
        self.nvlogin=self.nvconnector.dang_nhap(username,password)
        if self.nvlogin!=None:
            self.MainWindow.hide()
            self.mainwindow = QMainWindow()
            self.myui = MainProgramMainWindowExt()
            self.myui.setupUi(self.mainwindow)
            self.myui.showWindow()
        else:
            self.msg=QMessageBox()
            self.msg.setWindowTitle("Login thất bại")
            self.msg.setText("Bạn đăng nhập thất bại.\nKiểm tra lại thông tin đăng nhập")
            self.msg.setIcon(QMessageBox.Icon.Critical)
            self.msg.show()



