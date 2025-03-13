from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

from K22416C.SAKILA_BAITAP.Test.TestConnection import df1, df2, df3, df4

# Kết hợp các bảng
merged_df = df3.merge(df1, on="customer_id")          # Rental + Customer
merged_df = merged_df.merge(df2, on="inventory_id")   # Thêm Inventory
merged_df = merged_df.merge(df4, on="film_id", suffixes=('_left', '_right'))

# Tính toán các đặc trưng
features_df = merged_df.groupby("customer_id").agg(
    total_rentals=("rental_id", "count"),
    avg_film_length=("length", "mean"),
    avg_replacement_cost=("replacement_cost", "mean"),
    special_features_count=("special_features", lambda x: x.str.contains("Trailers").sum())
).reset_index()

scaler = StandardScaler()
scaled_data = scaler.fit_transform(features_df[["total_rentals", "avg_film_length", "avg_replacement_cost"]])

def elbowMethod(X):
    inertia = []
    for n in range(1, 11):
        model = KMeans(n_clusters=n, init='k-means++', max_iter=500, random_state=42)
        model.fit(X)
        inertia.append(model.inertia_)
    return inertia

def runKMeans(X, cluster):
    model = KMeans(n_clusters=cluster, init='k-means++', max_iter=500, random_state=42)
    model.fit(X)
    labels = model.labels_
    centroids = model.cluster_centers_
    y_kmeans = model.predict(X)
    return y_kmeans, centroids, labels