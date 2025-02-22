# Tách X, y từ df_topics
X = df_topics.drop(columns=["label"]).values  # Chuyển thành numpy array
y = df_topics["label"].values

# Chia tập train/test trước KHI scale và tạo cửa sổ
train_size = int(len(X) * 0.8)
X_train_raw, X_test_raw = X[:train_size], X[train_size:]
y_train_raw, y_test_raw = y[:train_size], y[train_size:]

# Scale dữ liệu RIÊNG BIỆT trên từng tập
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_raw)
X_test_scaled = scaler.transform(X_test_raw)

# Hàm tạo cửa sổ trượt (chỉ dùng features để tạo X_window)
def create_sliding_windows(features, labels, window_size):
    X, y = [], []
    for i in range(len(features) - window_size):
        X.append(features[i:i + window_size])
        y.append(labels[i + window_size])  # Nhãn từ biến y
    return np.array(X), np.array(y)

# Tạo cửa sổ cho train và test
window_size = 100
X_train, y_train = create_sliding_windows(X_train_scaled, y_train_raw, window_size)
X_test, y_test = create_sliding_windows(X_test_scaled, y_test_raw, window_size)