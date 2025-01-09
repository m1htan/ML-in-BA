import sqlite3
import pandas as pd

def NInvoice(Connection, n):
    """
    Return Customer with over N invoice
    """
    query = f'''
        SELECT i.CustomerID, FirstName, LastName, COUNT(*) as InvoiceCount
        FROM Invoice i
        JOIN Customer c ON c.CustomerID = i.CustomerID
        GROUP BY i.CustomerID
        HAVING COUNT(*) >= {n}
        '''
    cursor = Connection.cursor()
    cursor.execute(query)
    df = pd.DataFrame(cursor.fetchall())
    cursor.close()
    return df

def connect(database):
    try:
        Connection = sqlite3.connect('../Dataset/databases/Chinook_Sqlite.sqlite')
    except sqlite3.Error as error:
        print(f"Error: {error}")

    return Connection


if __name__ == "__main__":
    sqliteConnection = connect("Chinook_Sqlite")

    invoice_num = 5  # Giả sử là 5

    print(NInvoice(sqliteConnection, invoice_num))