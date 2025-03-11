import mysql.connector

class MySqlConnector:
    def __init__(self, server = None, port= None, database = None, username = None, password = None):
        if server == None:
            self.server = "localhost"
            self.port = 3306
            self.database = "K22416C_Sales"
            self.username = "root"
            self.password = "Minhtan0410@"
        else:
            self.server = server
            self.port = port
            self.database = database
            self.username = username
            self.password = password
    def connect(self):
        self.conn = mysql.connector.connect(
        host=self.server,
        port=self.port,
        database=self.database,
        user=self.username,
        password=self.password
        )
        return self.conn