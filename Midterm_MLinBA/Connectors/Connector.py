#python -m pip install mysql-connector-python
import mysql.connector
import traceback
import pandas as pd

class Connector:
    def __init__(self, server=None, port=None, database=None, username=None, password=None):
        if server==None:
            self.server = "localhost"
            self.port = 3306
            self.database = "retails"
            self.username = "root"
            self.password = "Minhtan0410@"
        else:
            self.server = server
            self.port = port
            self.database = database
            self.username = username
            self.password = password

        self.cursor = self.conn.cursor(dictionary=True)  # Trả về danh sách từ điển

    def connect(self):
        try:
            if hasattr(self, 'conn') and self.conn.is_connected():
                print("Đã kết nối trước đó, không cần kết nối lại.")
                return
            self.conn = mysql.connector.connect(host=self.server, port=self.port, database=self.database,
                                                user=self.username, password=self.password, auth_plugin='mysql_native_password')
        except mysql.connector.Error as err:
            print(f"Lỗi kết nối CSDL: {err}")

    def disConnect(self):
        if self.conn != None:
            self.conn.close()

    def queryDataset(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()  # Trả về danh sách từ điển chuẩn

    def getTablesName(self):
        cursor = self.conn.cursor()
        cursor.execute("Show tables;")
        results=cursor.fetchall()
        tablesName=[]
        for item in results:
            tablesName.append([tableName for tableName in item][0])
        return tablesName