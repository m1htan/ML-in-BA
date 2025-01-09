import sqlite3
import pandas as pd

sqliteConnection = None  # Khởi tạo biến sqliteConnection trước

try:
    # Kết nối đến cơ sở dữ liệu SQLite và tạo con trỏ
    sqliteConnection = sqlite3.connect('../Dataset/databases/Chinook_Sqlite.sqlite')
    cursor = sqliteConnection.cursor()
    print('DB Init')

    # Viết và thực thi câu truy vấn SQL
    query = 'SELECT * FROM InvoiceLine LIMIT 5;'
    cursor.execute(query)

    # Lấy kết quả và chuyển thành DataFrame
    columns = [desc[0] for desc in cursor.description]  # Lấy tên cột
    df = pd.DataFrame(cursor.fetchall(), columns=columns)
    print(df)

    # Đóng con trỏ
    cursor.close()

except sqlite3.Error as error:
    # Xử lý lỗi
    print('Error occurred -', error)

finally:
    # Đảm bảo đóng kết nối đến cơ sở dữ liệu dù có lỗi hay không
    if sqliteConnection:
        sqliteConnection.close()
        print('SQLite Connection closed')