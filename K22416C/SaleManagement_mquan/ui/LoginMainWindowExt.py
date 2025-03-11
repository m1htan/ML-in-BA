import traceback
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox, QMainWindow
from K22416C.SaleManagement_mquan.libs.nhanvienconnector import NhanVienConnector
from K22416C.SaleManagement_mquan.ui.LoginMainWindow import Ui_MainWindow
from K22416C.SaleManagement_mquan.ui.MainProgramMainWindowExt import MainProgramMainWindowExt


class LoginMainWindowExt(Ui_MainWindow):
    def __init__(self):
        self.nvconnector = NhanVienConnector()


    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButton.clicked.connect(self.xuly_dangnhap)

    def xuly_dangnhap(self):
        try:
            username = self.lineEdit.text()
            password = self.lineEdit_2.text()

            self.nvconnector.connect()
            self.nvlogin = self.nvconnector.dang_nhap(username, password)

            if self.nvlogin is not None:
                self.MainWindow.hide()
                self.mainwindow = QMainWindow()
                self.myui = MainProgramMainWindowExt()
                self.myui.setupUi(self.mainwindow)
                self.myui.showWindow()
            else:
                self.msg = QMessageBox()
                self.msg.setWindowTitle("Login thất bại")
                self.msg.setText("Bạn đăng nhập thất bại.\nKiểm tra lại thông tin đăng nhập")
                self.msg.setIcon(QMessageBox.Icon.Critical)
                self.msg.show()
        except Exception as e:
            print("Error:", e)
            traceback.print_exc()
