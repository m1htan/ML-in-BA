#python -m pip install mysql-connector-python
import mysql.connector
import traceback
import pandas as pd

class Connector:
    def __init__(self, server=None, port=None, database=None, username=None, password=None):
        if server==None:
            self.server = "localhost"
            self.port = 3306
            self.database = "Final_MLinBA"
            self.username = "root"
            self.password = "Minhtan0410@"
        else:
            self.server = server
            self.port = port
            self.database = database
            self.username = username
            self.password = password

    def connect(self):
        try:
            if hasattr(self, 'conn') and self.conn.is_connected():
                print("Đã kết nối trước đó, không cần kết nối lại.")
                return
            self.conn = mysql.connector.connect(host=self.server, port=self.port, database=self.database,
                                                user=self.username, password=self.password)
        except mysql.connector.Error as err:
            print(f"Lỗi kết nối CSDL: {err}")

    def disConnect(self):
        if self.conn != None:
            self.conn.close()

    def queryDataset(self, sql):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            df = pd.DataFrame(cursor.fetchall())
            if not df.empty:
                df.columns=cursor.column_names
            return df
        except:
            traceback.print_exc()
        return None

    def getTablesName(self):
        cursor = self.conn.cursor()
        cursor.execute("Show tables;")
        results=cursor.fetchall()
        tablesName=[]
        for item in results:
            tablesName.append([tableName for tableName in item][0])
        return tablesName