from PyQt6.QtWidgets import QTableWidgetItem
from Connectors.Connector import Connector
from MainWindow import Ui_MainWindow
import pandas as pd
import mysql.connector
import traceback


class Connector:
    def __init__(self, server=None, port=None, database=None, username=None, password=None):
        self.server = server
        self.port = port
        self.database = database
        self.username = username
        self.password = password
        self.conn = None

    def connect(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.server,
                port=self.port,
                database=self.database,
                user=self.username,
                password=self.password)
            return self.conn
        except Exception as e:
            print("Error connecting to MySQL:", e)
            traceback.print_exc()
            return None

    def disconnect(self):
        if self.conn is not None:
            self.conn.close()

    def execute(self, sql, values=None):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, values)
            self.conn.commit()
            print("SQL query executed successfully")
        except mysql.connector.Error as e:
            print("Error executing SQL query:", e)

    def queryDataset(self, sql):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            df = pd.DataFrame(cursor.fetchall())
            df.columns = cursor.column_names
            return df
        except Exception as e:
            print("Error querying dataset:", e)
            traceback.print_exc()
            return None


class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.connector = Connector(server="localhost", port=3306, database="babaecommerce", username="Quan",
                                   password="quan0508")

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButtonProduct.clicked.connect(self.loadProductIntoQTableWidget)
        self.pushButtonOrders.clicked.connect(self.loadOrders)
        self.pushButtoOrder_items.clicked.connect(self.loadOrder_items)
        self.pushButtoOrder_payments.clicked.connect(self.loadOrderPayments)
        self.pushButtonCustomers.clicked.connect(self.loadCustomer)
        self.pushButtonSellers.clicked.connect(self.loadSellers)
        self.pushButtonCalculate_a.clicked.connect(self.calculate_customer_purchase_over_years)
        self.pushButtonCalculate_b.clicked.connect(self.calculate_customer_purchase_growth_rate_over_years)
        self.pushButtonCalculate_c.clicked.connect(self.calculate_total_revenue_over_years)
        self.pushButtonCalculate_d.clicked.connect(self.calculate_total_revenue_by_category_year)
        self.pushButtonCalculate_e.clicked.connect(self.calculate_canceled_category_years)
        self.pushButtonFind.clicked.connect(self.findSellers())
        self.pushButtonFind_2.clicked.connect(self.findCustomer_Orders)
    def connectDatabase(self):
        self.connector.server = "localhost"
        self.connector.port = 3306
        self.connector.database = "babaecommerce"
        self.connector.username = "Quan"
        self.connector.password = "quan0508"
        self.connector.connect()

    def showDataIntoTableWidget(self, table, df):
        table.setRowCount(0)
        table.setColumnCount(len(df.columns))
        for i in range(len(df.columns)):
            columnHeader = df.columns[i]
            table.setHorizontalHeaderItem(i, QTableWidgetItem(columnHeader))
        row = 0
        for item in df.iloc:
            arr = item.values.tolist()
            table.insertRow(row)
            j = 0
            for data in arr:
                table.setItem(row, j, QTableWidgetItem(str(data)))
                j = j + 1
            row = row + 1

    def loadProductIntoQTableWidget(self):
        self.connectDatabase()
        sql = "select * from products"
        df = self.connector.queryDataset(sql)
        self.showDataIntoTableWidget(self.tableWidget, df)

    def loadCustomer(self):
        self.connectDatabase()
        sql = "select * from customers"
        df = self.connector.queryDataset(sql)
        self.showDataIntoTableWidget(self.tableWidget, df)

    def loadOrders(self):
        self.connectDatabase()
        sql = "select * from orders"
        df = self.connector.queryDataset(sql)
        self.showDataIntoTableWidget(self.tableWidget, df)

    def loadOrderPayments(self):
        self.connectDatabase()
        sql = "select * from order_payments"
        df = self.connector.queryDataset(sql)
        self.showDataIntoTableWidget(self.tableWidget, df)

    def loadSellers(self):
        self.connectDatabase()
        sql = "select * from sellers"
        df = self.connector.queryDataset(sql)
        self.showDataIntoTableWidget(self.tableWidget, df)

    def loadOrder_items(self):
        self.connectDatabase()
        sql = "select * from order_items"
        df = self.connector.queryDataset(sql)
        self.showDataIntoTableWidget(self.tableWidget, df)


    def calculate_customer_purchase_over_years(self):
        self.connectDatabase()
        sql = """
            SELECT 
            substring(orders.order_purchase_timestamp, 1, 4) as Year,
            COUNT(DISTINCT customers.customer_id) as Customers
            FROM orders
            JOIN customers ON customers.customer_id = orders.customer_id
            GROUP BY substring(orders.order_purchase_timestamp, 1, 4)
            """

        df = self.connector.queryDataset(sql)
        self.showDataIntoTableWidget(self.tableWidget, df)

    def calculate_customer_purchase_growth_rate_over_years(self):
        self.connectDatabase()
        sql= """
             SELECT 
             Year,
             Customers,
             (Customers - LAG(Customers, 1) OVER (ORDER BY Year)) as GrowthRate
             FROM (
             SELECT 
             substring(orders.order_purchase_timestamp, 1, 4) as Year,
             COUNT(DISTINCT customers.customer_id) as Customers
             FROM orders
             JOIN customers ON customers.customer_id = orders.customer_id
             GROUP BY substring(orders.order_purchase_timestamp, 1, 4)
             ) as T
             ORDER BY Year;
             """
        df = self.connector.queryDataset(sql)
        self.showDataIntoTableWidget(self.tableWidget,df)

    def calculate_total_revenue_over_years(self):
        self.connectDatabase()
        sql = """
             SELECT 
             substring(orders.order_purchase_timestamp, 1, 4) as Year,
             sum(order_payments.payment_value) as TotalRevenue
             FROM orders
             JOIN customers ON customers.customer_id = orders.customer_id
             JOIN order_payments ON order_payments.order_id = orders.order_id
             GROUP BY substring(orders.order_purchase_timestamp, 1, 4) 
             ORDER BY Year;
              """
        df = self.connector.queryDataset(sql)
        self.showDataIntoTableWidget(self.tableWidget, df)

    def calculate_total_revenue_by_category_year(self):
        self.connectDatabase()
        sql = """
                SELECT 
                substring(orders.order_purchase_timestamp, 1, 4) as Year,
                sum(order_payments.payment_value) as TotalRevenue,
                products.product_category_name
                FROM orders
                JOIN customers ON customers.customer_id = orders.customer_id
                JOIN order_payments ON order_payments.order_id = orders.order_id
                JOIN order_items ON order_items.order_id = orders.order_id
                JOIN products ON products.product_id = order_items.product_id
                GROUP BY substring(orders.order_purchase_timestamp, 1, 4),
                products.product_category_name 
                ORDER BY Year;
                """
        df = self.connector.queryDataset(sql)
        self.showDataIntoTableWidget(self.tableWidget, df)

    def calculate_canceled_category_years(self):
        self.connectDatabase()
        sql = """
                        SELECT 
                        substring(orders.order_purchase_timestamp, 1, 4) as Year,
                        sum(order_payments.payment_value) as TotalRevenue,
                        products.product_category_name
                        FROM orders
                        JOIN customers ON customers.customer_id = orders.customer_id
                        JOIN order_payments ON order_payments.order_id = orders.order_id
                        JOIN order_items ON order_items.order_id = orders.order_id
                        JOIN products ON products.product_id = order_items.product_id
                        GROUP BY substring(orders.order_purchase_timestamp, 1, 4),
                        products.product_category_name 
                        ORDER BY Year;
                        """
        df = self.connector.queryDataset(sql)
        self.showDataIntoTableWidget(self.tableWidget, df)


    def findSellers(self):
        seller_state = self.lineEditCusID.text()  # Assuming lineEditCusID is the input field

        # Validate customer ID input (optional)
        try:
            int(seller_state)  # Check if it's a valid integer
        except ValueError:

            return

        sql = f"SELECT seller_id, seller,seller_zip_code_prefix, seller_city FROM Sellers WHERE seller_state = {seller_state}"
        df = self.connector.queryDataset(sql)

        if df is not None and not df.empty:  # Check if customer exists
            self.label_Status.setText("Seller information found and displayed.")
        else:
            self.label_Status.setText("Seller not found.")


    def findCustomer_Orders(self):
        customer_id = self.lineEditCusID.text()  # Assuming lineEditCusID is the input field

            # Validate customer ID input (optional)
        try:
            int(customer_id)  # Check if it's a valid integer
        except ValueError:
            self.label_Status_2.setText("Invalid Customer ID. Please enter a number.")
            return

        sql = f"""
                SELECT orders.OrderID, orders.OrderDate, orders.DueDate, orders.ShipDate
                FROM Orders 
                JOIN Customer ON orders.CustomerID = customer.CustomerID
                WHERE customer.CustomerID = {customer_id}
                """

        df = self.connector.queryDataset(sql)

        if df is not None and not df.empty:
            self.showDataIntoTableWidget(self.tableWidget, df)
            self.label_Status_2.setText("Customer orders found and displayed.")
        else:
            self.label_Status_2.setText("Customer has no orders.")
            self.tableWidget.setRowCount(0)

    def show(self):
        self.MainWindow.show()