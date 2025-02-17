import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QInputDialog, QApplication, QWidget, QGridLayout, QListWidget, QPushButton, QLabel, \
    QListWidgetItem, QMessageBox
from PyQt6.QtGui import QIcon


# Bước 1: Tạo đối tượng QListWidget
self.list_widget = QListWidget(self)


# Bước 2: Gọi các hàm addItem, addItems để thêm item vào QListWidget
self.list_widget.addItems(["Learn Python","Machine Learning","Deep Learning"])
self.list_widget.addItem("Smart Contract")

item=QListWidgetItem()
item.setText("Metaverse")
item.setIcon(QIcon("images/ic_metaverse.png"))
item.setForeground(Qt.GlobalColor.red)
item.setBackground(Qt.GlobalColor.yellow)
self.list_widget.addItem(item)


# Bước 3: Để chèn item vào QListWidget ta dùng hàm insertItem. Hàm này có 2 đối số, đối số 1 là vị trí muốn chèn, đối số 2 là giá trị muốn chèn. Ví dụ dưới đây sẽ chèn item vào vị trí đằng sau dòng mà người dùng đang chọn:
item="Value or QListWidgetItem"
current_row = self.list_widget.currentRow()
self.list_widget.insertItem(current_row+1, item)


# Bước 4: Để chỉnh sửa Item trong QListWidget ta làm như sau:
updatedItem=self.list_widget.item(0)
updatedItem.setText("New value for item at row 0")


# Bước 5: Để xóa item đang chọn ra khỏi QListWidget ta gọi lệnh takeItem
current_row = self.list_widget.currentRow()
if current_row >= 0:
    current_item = self.list_widget.takeItem(current_row)
    del current_item

# Bước 6: Để xóa toàn bộ item ra khỏi QListWidget ta gọi lệnh clear():
self.list_widget.clear()