import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

from MLinBA.Midterm_MLinBA.Connectors.Connector import Connector
from MLinBA.Midterm_MLinBA.Model.Prepare.Statistic import Statistic


class CustomerSegmentation:
    def __init__(self, connector, n_clusters=3):
        self.connector = connector
        self.n_clusters = n_clusters
        self.model = None
        self.customer_clusters = None

    import pandas as pd

    def load_data_CS(self):
        sql = """
        SELECT c.CustomerID, COUNT(o.OrderID) AS TotalOrders, 
               SUM(od.OrderQty * od.UnitPrice) AS TotalSpent,
               COUNT(DISTINCT od.ProductID) AS UniqueProducts
        FROM customer c
        LEFT JOIN orders o ON c.CustomerID = o.CustomerID
        LEFT JOIN orderdetails od ON o.OrderID = od.OrderID
        GROUP BY c.CustomerID
        """
        data = self.connector.queryDataset(sql)

        # Kiểm tra kiểu dữ liệu của data
        print("Raw data type:", type(data))
        print("Raw data sample:", data[:5])  # Xem 5 dòng đầu tiên nếu là list

        # Kiểm tra nếu dữ liệu rỗng hoặc không đúng định dạng
        if not isinstance(data, list) or len(data) == 0:
            print("⚠️ No data returned from SQL query!")
            return pd.DataFrame(columns=["CustomerID", "TotalOrders", "TotalSpent", "UniqueProducts"])

        # Nếu data là danh sách tuple, chuyển thành DataFrame
        df = pd.DataFrame(data, columns=["CustomerID", "TotalOrders", "TotalSpent", "UniqueProducts"])

        # Kiểm tra DataFrame sau khi chuyển đổi
        print("DataFrame Loaded:\n", df.head())

        return df

    def train_model(self, data):
        scaler = StandardScaler()
        features = ["TotalOrders", "TotalSpent", "UniqueProducts"]
        self.df_scaled = scaler.fit_transform(data[features])

        self.model = KMeans(n_clusters=self.n_clusters, random_state=42)
        data["Cluster"] = self.model.fit_predict(self.df_scaled)
        self.customer_clusters = data[["CustomerID", "Cluster"]]

    def get_customers_by_cluster(self, cluster_id):
        return self.customer_clusters[self.customer_clusters["Cluster"] == cluster_id]


# Kết nối database
conn = Connector()
conn.connect()

# Khởi tạo phân cụm khách hàng
segmentation = CustomerSegmentation(conn)

# Lấy dữ liệu
data = segmentation.load_data_CS()

# Huấn luyện mô hình
segmentation.train_model(data)

# Lấy danh sách khách hàng từ cụm 1
print(segmentation.get_customers_by_cluster(1))
