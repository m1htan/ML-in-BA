from PyQt6.QtWidgets import QMessageBox, QMainWindow

from MLinBA.Final_MLinBA.UI.LoginWindow import Ui_LoginWindow
from MLinBA.Final_MLinBA.Connectors.Connector import Connector


class LoginWindowExt(Ui_LoginWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.LoginWindow = QMainWindow()
        self.setupUi(self.LoginWindow)
        self.parent=None

    def setupUi(self, LoginWindow):
        super().setupUi(LoginWindow)
        self.LoginWindow=LoginWindow
        self.pushButtonConnect.clicked.connect(self.connectDatabase)

    def get_main_window_ext(self):
        from MLinBA.Final_MLinBA.UI.MainWindowExt import MainWindowExt
        return MainWindowExt()

    def connectDatabase(self):
        try:
            # Lấy thông tin từ các ô nhập liệu
            server = self.lineEditServer.text()
            port = int(self.lineEditPort.text())
            database = self.lineEditDatabase.text()
            username = self.lineEditUser.text()
            password = self.lineEditPassword.text()

            # Tạo đối tượng Connector với thông tin mặc định
            default_connector = Connector()

            # So sánh thông tin người dùng nhập với thông tin mặc định
            if (server == default_connector.server and
                port == default_connector.port and
                database == default_connector.database and
                username == default_connector.username and
                password == default_connector.password):

                # Kết nối đến cơ sở dữ liệu
                self.connector = Connector(server, port, database, username, password)
                self.connector.connect()

                # Hiển thị thông báo kết nối thành công
                self.msg = QMessageBox()
                self.msg.setText("Connect database successful!")
                self.msg.setWindowTitle("Info")
                self.msg.setIcon(QMessageBox.Icon.Information)
                self.msg.show()

                # Chuyển đến MainWindow nếu đang ở trang Login
                if self.connector != None:
                    self.LoginWindow.hide()
                    self.mainwindow = self.get_main_window_ext()
                    self.mainwindow.show()

            else:
                # Hiển thị thông báo lỗi nếu thông tin không khớp
                self.msg = QMessageBox()
                self.msg.setWindowTitle("Connection fail")
                self.msg.setText("Kết nối thất bại.\nThông tin kết nối không khớp với thông tin mặc định.")
                self.msg.setIcon(QMessageBox.Icon.Critical)
                self.msg.show()

        except Exception as e:
            # Xử lý lỗi nếu có
            self.msg = QMessageBox()
            self.msg.setWindowTitle("Connection fail")
            self.msg.setText(f"Kết nối thất bại.\nLỗi: {str(e)}")
            self.msg.setIcon(QMessageBox.Icon.Critical)
            self.msg.show()

    def showWindow(self):
        self.LoginWindow.show()




