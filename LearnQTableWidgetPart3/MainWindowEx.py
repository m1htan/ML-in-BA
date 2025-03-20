import os.path

from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtWidgets import QFileDialog, QTableWidgetItem, QMessageBox
from MainWindow import Ui_MainWindow

class MainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.pushButtonPickSQLite.clicked.connect(self.processPickSQLite)
        self.cboTable.activated.connect(self.processSelectedTable)
        self.pushButtonFetchMore.clicked.connect(self.processFetchMore)
        self.model=None
    def processPickSQLite(self):
        #setup for QFileDialog
        filters = "SQLite database (*.sqlite);;All files(*)"
        filename, selected_filter = QFileDialog.getOpenFileName(
            self.MainWindow,
            filter=filters,
        )
        #get selected file name and showing on the QLineEdit
        self.lineEditSQLite.setText(filename)
        #create base dir
        baseDir = os.path.dirname(__file__)
        #set the database path
        databasePath = os.path.join(baseDir, filename)
        #create QSqlDatabase object
        self.db = QSqlDatabase("QSQLITE")
        #set the database selected path
        self.db.setDatabaseName(databasePath)
        #Open the SQLite database
        self.db.open()
        #get all tables in the selected SQLite
        tables= self.db.tables()
        self.cboTable.clear()
        #show all the table names into the QCombobox:
        for i in range(len(tables)):
            tableName=tables[i]
            self.cboTable.addItem(tableName)
    def processSelectedTable(self):
        #Get the current Table Name in QCombobox
        tableName=self.cboTable.currentText()
        #Create QSqlTableModel object, and self.db is assigned
        self.model = QSqlTableModel(db=self.db)
        #select table name to invoke data
        self.model.setTable(tableName)
        #active for selecting data
        self.model.select()
        #reset QTableWidget to 0 row
        self.tableWidget.setRowCount(0)
        #get the column count for selected Table as automatic
        self.columns=self.model.record().count()
        #set columns count for QTableWidget
        self.tableWidget.setColumnCount(self.columns)
        #create labels array for Columns Headers
        labels=[]
        for i in range(self.columns):
            #get column name:
            fieldName=self.model.record().fieldName(i)
            #store the column name
            labels.append(fieldName)
        #set the columns header with labels
        self.tableWidget.setHorizontalHeaderLabels(labels)
        #loop for insert new row:
        for i in range(self.model.rowCount()):
            #insert new row:
            self.tableWidget.insertRow(i)
            #get a record with i index:
            record=self.model.record(i)
            #loop column to get value for each cell:
            for j in range(self.columns):
                #create QTableWidgetItem object
                item=QTableWidgetItem(str(record.value(j)))
                #set value for each CELL:
                self.tableWidget.setItem(i,j,item)
    def processFetchMore(self):
        #check if the model can fetch more:
        if self.model.canFetchMore():
            #set the i index for last rowcount:
            i=self.model.rowCount()
            #call fetchmore method:
            self.model.fetchMore()
            #loop for new batch data:
            for i in range(i,self.model.rowCount()):
                # insert new row:
                self.tableWidget.insertRow(i)
                # get a record with i index:
                record = self.model.record(i)
                # loop column to get value for each cell:
                for j in range(self.columns):
                    # create QTableWidgetItem object
                    item = QTableWidgetItem(str(record.value(j)))
                    # set value for each CELL:
                    self.tableWidget.setItem(i, j, item)
        else:
            msg=QMessageBox()
            msg.setText("No more records to fetch")
            msg.exec()
    def show(self):
        self.MainWindow.show()