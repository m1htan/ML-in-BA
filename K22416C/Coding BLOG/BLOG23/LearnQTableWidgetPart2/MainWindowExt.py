from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox

from FileFactory import FileFactory
from MainWindow import Ui_MainWindow
from Product import Product


class MainWindowExt(Ui_MainWindow):
    def __init__(self):
        self.products=[]
        self.selectedProduct=None
        self.fileFactory=FileFactory()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.products=self.fileFactory.readData("database.json",Product)
        self.loadDataIntoTableWidget()
        self.pushButtonNew.clicked.connect(self.processNew)
        self.pushButtonSave.clicked.connect(self.processSave)
        self.tableWidgetProduct.itemSelectionChanged.connect(self.processItemSelection)
        self.pushButtonRemove.clicked.connect(self.processDelete)
    def loadDataIntoTableWidget(self):
        self.tableWidgetProduct.setRowCount(0)
        for i in range(len(self.products)):
            product=self.products[i]
            row = self.tableWidgetProduct.rowCount()
            self.tableWidgetProduct.insertRow(row)
            self.tableWidgetProduct.setItem(row, 0, QTableWidgetItem(str(product.ProductId)))
            self.tableWidgetProduct.setItem(row, 1, QTableWidgetItem(product.ProductName))
            itemPrice = QTableWidgetItem()
            itemPrice.setText(str(product.Price))
            if product.Price < 10000000:
                itemPrice.setForeground(Qt.GlobalColor.red)
                itemPrice.setBackground(Qt.GlobalColor.yellow)
            self.tableWidgetProduct.setItem(row, 2, itemPrice)
    def processNew(self):
        self.lineEditProductId.setText("")
        self.lineEditProductName.setText("")
        self.lineEditUnitPrice.setText("")
        self.lineEditProductId.setFocus()
        self.selectedProduct=None
    def processSave(self):
        product=Product(self.lineEditProductId.text(),self.lineEditProductName.text(),float(self.lineEditUnitPrice.text()))
        if self.selectedProduct==None:
            self.products.append(product)
            row = self.tableWidgetProduct.rowCount()
            self.tableWidgetProduct.insertRow(row)
        else:
            row=self.products.index(self.selectedProduct)
        self.selectedProduct = product
        self.products[row] = self.selectedProduct
        self.tableWidgetProduct.setItem(row,0,QTableWidgetItem(str(product.ProductId)))
        self.tableWidgetProduct.setItem(row,1,QTableWidgetItem(product.ProductName))
        itemPrice=QTableWidgetItem()
        itemPrice.setText(str(product.Price))
        if product.Price<10000000:
            itemPrice.setForeground(Qt.GlobalColor.red)
            itemPrice.setBackground(Qt.GlobalColor.yellow)
        self.tableWidgetProduct.setItem(row, 2, itemPrice)
        self.fileFactory.writeData("database.json", self.products)
    def processItemSelection(self):
        row=self.tableWidgetProduct.currentRow()
        if row ==-1 or row>=len(self.products):
            return
        #id=self.tableWidgetProduct.item(row,0).text()
        #name=self.tableWidgetProduct.item(row,1).text()
        #price = self.tableWidgetProduct.item(row, 2).text()
        product=self.products[row]
        self.selectedProduct=product
        id=product.ProductId
        name=product.ProductName
        price=product.Price
        self.lineEditProductId.setText(str(id))
        self.lineEditProductName.setText(name)
        self.lineEditUnitPrice.setText(str(price))
    def processDelete(self):
        dlg = QMessageBox(self.MainWindow)
        if self.selectedProduct == None:
            dlg.setWindowTitle("Deleteing error")
            dlg.setIcon(QMessageBox.Icon.Critical)
            dlg.setText("You have to select a Product to delete")
            dlg.exec()
            return
        dlg.setWindowTitle("Confirmation Deleting")
        dlg.setText("Are you sure you want to delete?")
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        dlg.setStandardButtons(buttons)
        button = dlg.exec()
        if button == QMessageBox.StandardButton.Yes:
            row=self.products.index(self.selectedProduct)
            self.products.remove(self.selectedProduct)
            self.selectedProduct=None
            self.tableWidgetProduct.removeRow(row)
            self.processNew()
            self.fileFactory.writeData("database.json", self.products)
    def show(self):
        self.MainWindow.show()