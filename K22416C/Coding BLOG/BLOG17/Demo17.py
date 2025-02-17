import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QInputDialog, QApplication, QWidget, QGridLayout, QListWidget, QPushButton, QLabel, \
    QListWidgetItem, QMessageBox
from PyQt6.QtGui import QIcon

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('QListWidget Demo')
        self.setWindowIcon(QIcon('images/ic_logo.jpg'))
        self.setGeometry(100, 100, 400, 100)

        layout = QGridLayout(self)
        self.setLayout(layout)

        self.list_widget = QListWidget(self)
        #Create a QListWidgetItem and set the attributes
        newItem = QListWidgetItem()
        newItem.setText("Metaverse")
        newItem.setIcon(QIcon('images/ic_metaverse.png'))
        newItem.setForeground(Qt.GlobalColor.red)
        newItem.setBackground(Qt.GlobalColor.yellow)
        newItem.setCheckState(Qt.CheckState.Checked)
        #add new QListWidgetItem
        self.list_widget.addItem(newItem)

        #add a text for a new QlistWidgetItem
        self.list_widget.addItem("Smart Contract")
        #get item at row 1 and set icon for this Item
        self.list_widget.item(1).setIcon(QIcon('images/ic_smartcontract.png'))
        #add an array for QListWidget
        self.list_widget.addItems(["Learn Python", "Machine Learning", "Deep Learning"])

        layout.addWidget(self.list_widget, 0, 0, 5, 1)
        # create buttons and do signals and slots for QPushButton action:
        add_button = QPushButton('Add New Item')
        add_button.clicked.connect(self.addItem)

        update_button = QPushButton('Update Item')
        update_button.clicked.connect(self.updateItem)

        insert_button = QPushButton('Insert New Item')
        insert_button.clicked.connect(self.insertItem)

        remove_button = QPushButton('Remove Selected Item')
        remove_button.clicked.connect(self.removeItem)

        clear_button = QPushButton('Clear All')
        clear_button.clicked.connect(self.clearAll)

        layout.addWidget(add_button, 0, 1)
        layout.addWidget(update_button, 1, 1)
        layout.addWidget(insert_button, 2, 1)
        layout.addWidget(remove_button, 3, 1)
        layout.addWidget(clear_button, 4, 1)
        #mouse and key signal for QListWidget
        self.list_widget.itemClicked.connect(self.processItemClicked)
        self.list_widget.itemDoubleClicked.connect(self.processItemDoubleClicked)
        #Signal listener user selected the item
        self.list_widget.itemSelectionChanged.connect(self.processItemSelectionChanged)
        # show the window
        self.show()
    #slot to show text of selected item into the title of Window
    def processItemSelectionChanged(self):
        current_row = self.list_widget.currentRow()
        item = self.list_widget.item(current_row)
        self.setWindowTitle(item.text())
    #slot show the update ui:
    def processItemDoubleClicked(self):
        self.updateItem()
    #slot for clicking the item
    def processItemClicked(self):
        current_row = self.list_widget.currentRow()
        data = self.list_widget.item(current_row)
        print("itemClicked=",data.text())
    #slot to show Adding new Item for QListWidget, using QInputDialog
    def addItem(self):
        text, ok = QInputDialog.getText(self, 'Add a New Data', 'New Data:')
        if ok and text:
            self.list_widget.addItem(text)

    # slot to show Updating selected Item for QListWidget, using QInputDialog
    def updateItem(self):
        current_row = self.list_widget.currentRow()
        if current_row >= 0:
            item = self.list_widget.item(current_row)
            text, ok = QInputDialog.getText(self, 'Update Data', 'New Data:',text=item.text())
            if ok and text:
                item.setText(text)

    # slot to show Inserting a new Item for QListWidget, using QInputDialog
    def insertItem(self):
        text, ok = QInputDialog.getText(self, 'Insert a New Data', 'New Data:')
        if ok and text:
            current_row = self.list_widget.currentRow()
            self.list_widget.insertItem(current_row+1, text)
    #slot to remove selected item
    def removeItem(self):
        current_row = self.list_widget.currentRow()
        if current_row >= 0:
            item=self.list_widget.item(current_row)
            msg=QMessageBox()
            msg.setText(f"Are you sure you want to remove {item.text()}?")
            msg.setWindowTitle("Removing Confirmation")
            msg.setIcon(QMessageBox.Icon.Question)
            buttons=QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.No
            msg.setStandardButtons(buttons)
            result= msg.exec()
            if result==QMessageBox.StandardButton.Yes:
                current_item = self.list_widget.takeItem(current_row)
                del current_item
    #slot to remove all item from QListWidget
    def clearAll(self):
        answer = QMessageBox.question(
            self,
            'Confirmation',
            'Do you want to clear all Data?',
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )
        if answer == QMessageBox.StandardButton.Yes:
            self.list_widget.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())