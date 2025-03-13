from flask import Flask
from flaskext.mysql import MySQL
import pandas as pd

app = Flask(__name__)

def getConnect(server, port, database, username, password):
    global mysql
    try:
        mysql = MySQL()
        # MySQL configurations
        app.config['MYSQL_DATABASE_HOST'] = server
        app.config['MYSQL_DATABASE_PORT'] = port
        app.config['MYSQL_DATABASE_DB'] = database
        app.config['MYSQL_DATABASE_USER'] = username
        app.config['MYSQL_DATABASE_PASSWORD'] = password
        mysql.init_app(app)
        conn = mysql.connect()
        return conn
    except mysql.connector.Error as e:
        print("Error = ", e)
    return None

def closeConnection(conn):
    if conn != None:
        conn.close()


def queryDataset(conn, sql):
    cursor = conn.cursor()
    cursor.execute(sql)

    # Lấy tên cột từ MySQL
    columns = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(cursor.fetchall(), columns=columns)

    return df
