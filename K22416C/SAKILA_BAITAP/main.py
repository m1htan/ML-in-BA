from matplotlib import pyplot as plt

from K22416C.SAKILA_BAITAP.Models.KMeans import elbowMethod, scaled_data, runKMeans, features_df

# Bước 1: Xác định số cụm bằng Elbow Method
inertia = elbowMethod(scaled_data)
plt.plot(range(1, 11), inertia, marker='o')
plt.xlabel('Số cụm (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method')
plt.show()

# Bước 2: Huấn luyện mô hình
k = 4
y_kmeans, centroids, labels = runKMeans(scaled_data, k)

# Thêm nhóm vào DataFrame
features_df["cluster"] = labels
print(features_df.head())

features_df.to_csv("clustering_results.csv", index=False)
print("Đã lưu kết quả vào clustering_results.csv")
