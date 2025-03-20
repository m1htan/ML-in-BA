import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

from MLinBA.Midterm_MLinBA.Connectors.Connector import Connector


class SalesForecast:
    def __init__(self, connector):
        self.connector = connector
        self.model = None

    def load_data(self):
        sql = """
        SELECT o.OrderDate, c.CategoryID, SUM(od.OrderQty * od.UnitPrice) AS TotalRevenue
        FROM orders o
        JOIN orderdetails od ON o.OrderID = od.OrderID
        JOIN product p ON od.ProductID = p.ProductID
        JOIN subcategory sc ON p.ProductSubcategoryID = sc.SubcategoryID
        JOIN category c ON sc.CategoryID = c.CategoryID
        GROUP BY o.OrderDate, c.CategoryID
        ORDER BY o.OrderDate
        """
        self.df = self.connector.queryDataset(sql)
        self.df["OrderDate"] = pd.to_datetime(self.df["OrderDate"])
        self.df["Days"] = (self.df["OrderDate"] - self.df["OrderDate"].min()).dt.days

    def train_model(self, category_id):
        df_cat = self.df[self.df["CategoryID"] == category_id]

        X = df_cat[["Days"]]
        y = df_cat["TotalRevenue"]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model = LinearRegression()
        self.model.fit(X_train, y_train)

        y_pred = self.model.predict(X_test)
        print("MAE:", mean_absolute_error(y_test, y_pred))

    def predict_sales(self, future_days):
        future_X = np.array(future_days).reshape(-1, 1)
        predictions = self.model.predict(future_X)
        return predictions

# Kết nối database
conn = Connector()
conn.connect()

# Khởi tạo và huấn luyện mô hình
forecast = SalesForecast(conn)
forecast.load_data()
forecast.train_model(category_id=1)  # Dự báo cho danh mục có ID = 1

# Dự báo doanh thu trong 30 ngày tới
print(forecast.predict_sales([400, 410, 420]))