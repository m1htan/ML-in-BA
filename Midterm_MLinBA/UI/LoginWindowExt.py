from PyQt6.QtWidgets import QMessageBox, QMainWindow

from UI.LoginWindow import Ui_LoginWindow
from Connectors.Connector import Connector


class LoginWindowExt(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.connector = None

        self.ui.pushButtonConnect.clicked.connect(self.connectDatabase)

    def connectDatabase(self):
        try:
            # Lấy thông tin từ các ô nhập liệu
            server = self.ui.lineEditServer.text()
            port = int(self.ui.lineEditPort.text())
            database = self.ui.lineEditDatabase.text()
            username = self.ui.lineEditUser.text()
            password = self.ui.lineEditPassword.text()

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
                self.hide()
                from MLinBA.Midterm_MLinBA.UI.MainWindowExt import MainWindowExt
                self.mainwindow = MainWindowExt()
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
        self.show()




