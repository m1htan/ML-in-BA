import traceback

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import mysql.connector

from MLinBA.Midterm_MLinBA.Connectors.Connector import Connector


class Statistic(Connector):
    def __init__(self, connector=None):
        super().__init__()
        self.connector = connector

        self.df_total_sales = None
        self.df_revenue_by_category = None
        self.df_revenue_by_category_month = None
        self.df_early_delivered_orders = None
        self.df_customer_details = None
        self.df_customer_orders = None

    def execPurchaseHistory(self,tableName=None):
        if tableName==None:
            sql="select * from retails"
        else:
            sql = "select * from %s"%tableName
        self.df=self.connector.queryDataset(sql)
        self.lasted_df=self.df
        return self.df

    def connect(self):
        try:
            if hasattr(self, 'conn') and self.conn.is_connected():
                print("Đã kết nối trước đó, không cần kết nối lại.")
                return
            self.conn = mysql.connector.connect(host=self.server, port=self.port, database=self.database,
                                                user=self.username, password=self.password)
        except mysql.connector.Error as err:
            print(f"Lỗi kết nối CSDL: {err}")

    def queryDataset(self, sql):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            df = pd.DataFrame(cursor.fetchall())
            if not df.empty:
                df.columns=cursor.description
            return df
        except:
            traceback.print_exc()
        return None

    def printHead(self,row):
        print(self.df.head(row))

    def printTail(self,row):
        print(self.df.tail(row))

    def printInfo(self):
        print(self.df.info())

    def printDescribe(self):
        print(self.df.describe())

    def visualizePieChart(self,df,columnLabel,columnStatistic,title,legend=True):
        explode=[0.1]
        for i in range(len(df[columnLabel])-1):
            explode.append(0)
        plt.figure(figsize=(8, 6))
        plt.pie(df[columnStatistic], labels=df[columnLabel], autopct='%1.2f%%',explode=explode)
        if legend:
            plt.legend(df[columnLabel])
        plt.title(title)
        plt.show()

    def visualizePlotChart(self,df,columnX,columnY,title):
        plt.figure(figsize=(8, 6))
        plt.plot(df[columnX], df[columnY])
        plt.legend([columnX,columnY])
        plt.title(title)
        plt.xlabel(columnX)
        plt.ylabel(columnY)
        plt.grid()
        plt.show()

    def visualizeCountPlot(self,df,columnX,columnY,hueColumn,title):
        plt.figure(figsize=(8, 6))
        ax=sns.countplot(x=columnX,hue=hueColumn,data=df)
        plt.title(title)
        plt.xlabel(columnX)
        plt.ylabel(columnY)
        plt.grid()
        plt.legend()
        plt.show()

    def visualizeBarPlot(self,df,columnX,columnY,hueColumn,title,alpha=0.8,width=0.6):
        plt.figure(figsize=(8, 6))
        plt.ticklabel_format(useOffset=False, style='plain')
        ax=sns.barplot(data=df,x=columnX,y=columnY,hue=hueColumn,alpha=alpha,width=width)
        plt.title(title)
        plt.xlabel(columnX)
        plt.ylabel(columnY)
        plt.grid()
        plt.legend()
        plt.show()

    def visualizeBarChart(self,df,columnX,columnY,title):
        plt.figure(figsize=(8, 6))
        plt.ticklabel_format(useOffset=False, style='plain')
        plt.bar(df[columnX],df[columnY])
        plt.title(title)
        plt.xlabel(columnX)
        plt.ylabel(columnY)
        plt.grid()
        plt.show()

    def visualizeScatterPlot(self,df,columnX,columnY,title):
        plt.figure(figsize=(8, 6))
        plt.ticklabel_format(useOffset=False, style='plain')
        sns.scatterplot(data=df,x= columnX,y=columnY)
        plt.title(title)
        plt.xlabel(columnX)
        plt.ylabel(columnY)
        plt.grid()
        plt.show()

    # Câu 2: Thống kê tổng doanh số bán hàng của khách hàng
    def getTotalSalesByProduct(self):
        query = """
        SELECT 
            c.CustomerID,
            c.FirstName,
            c.LastName,
            SUM(od.OrderQty * od.UnitPrice) AS TotalSales
        FROM orders o
        JOIN orderdetails od ON o.OrderID = od.OrderID
        JOIN customer c ON o.CustomerID = c.CustomerID
        GROUP BY c.CustomerID, c.FirstName, c.LastName
        ORDER BY TotalSales DESC;
        """
        self.df_total_sales = pd.DataFrame.from_records(self.connector.queryDataset(query))
        return self.df_total_sales

    # Câu 3: Thống kê tổng doanh thu theo từng danh mục
    def getTotalRevenueByCategory(self):
        query = """
        SELECT 
            c.Name AS CategoryName,
            SUM(od.OrderQty * od.UnitPrice) AS TotalRevenue
        FROM orderdetails od
        JOIN product p ON od.ProductID = p.ProductID
        JOIN subcategory sc ON p.ProductSubcategoryID = sc.SubcategoryID
        JOIN category c ON sc.CategoryID = c.CategoryID
        GROUP BY c.Name
        ORDER BY TotalRevenue DESC;
        """
        self.df_revenue_by_category = pd.DataFrame.from_records(self.connector.queryDataset(query))
        return self.df_revenue_by_category

    # Câu 4: Thống kê tổng doanh thu theo danh mục, phân theo Tháng + Năm
    def getTotalRevenueByCategoryAndMonth(self):
        query = """
        SELECT c.Name AS CategoryName, 
               DATE_FORMAT(STR_TO_DATE(o.OrderDate, '%d/%m/%Y'), '%Y-%m') AS YearMonth, 
               SUM(od.OrderQty * od.UnitPrice) AS TotalRevenue
        FROM orderdetails od
        JOIN orders o ON od.OrderID = o.OrderID
        JOIN product p ON od.ProductID = p.ProductID
        JOIN subcategory s ON p.ProductSubcategoryID = s.SubcategoryID
        JOIN category c ON s.CategoryID = c.CategoryID
        GROUP BY c.Name, YearMonth
        ORDER BY YearMonth;
        """
        self.df_revenue_by_category_month = pd.DataFrame.from_records(self.connector.queryDataset(query))
        return self.df_revenue_by_category_month

    # Câu 5: Thống kê các đơn hàng giao nhanh trước hạn từ 3 ngày trở lên
    def getEarlyDeliveredOrders(self):
        query = """
        SELECT OrderID, 
            STR_TO_DATE(OrderDate, '%d/%m/%Y') AS OrderDate, 
            STR_TO_DATE(DueDate, '%d/%m/%Y') AS DueDate, 
            STR_TO_DATE(ShipDate, '%d/%m/%Y') AS ShipDate,
            DATEDIFF(STR_TO_DATE(DueDate, '%d/%m/%Y'), STR_TO_DATE(ShipDate, '%d/%m/%Y')) AS DaysEarly
        FROM orders
        WHERE DATEDIFF(STR_TO_DATE(DueDate, '%d/%m/%Y'), STR_TO_DATE(ShipDate, '%d/%m/%Y')) >= 3;
        """
        self.df_early_delivered_orders = pd.DataFrame.from_records(self.connector.queryDataset(query))
        return self.df_early_delivered_orders
