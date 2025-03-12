from imblearn.over_sampling import BorderlineSMOTE
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt

from MLinBA.Final_MLinBA.Dataset.PrepareData import X, y

# Chia tập train-test với stratify
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# Thử Borderline-SMOTE thay vì SMOTE chuẩn
sm = BorderlineSMOTE(sampling_strategy=0.5, random_state=42)
X_train_os, y_train_os = sm.fit_resample(X_train, y_train)

# Chuẩn hóa dữ liệu
scaler = StandardScaler()
X_train_os = scaler.fit_transform(X_train_os)
X_test = scaler.transform(X_test)  # Chỉ transform tập test, không fit lại!

# Huấn luyện mô hình
model = LogisticRegression(C=0.1, solver='liblinear', max_iter=500)
model.fit(X_train_os, y_train_os)

# Dự đoán và đánh giá
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# ĐÁNH GIÁ MODEL
# Dự đoán xác suất
y_probs = model.predict_proba(X_test)[:, 1]  # Xác suất của lớp dương (1)

# Tính toán các chỉ số đánh giá
mae = round(metrics.mean_absolute_error(y_test, y_pred), 4)
mse = round(metrics.mean_squared_error(y_test, y_pred), 4)
rmse = round(np.sqrt(mse), 4)

# Tính ROC-AUC
fpr, tpr, _ =  metrics.roc_curve(y_test, y_probs)
roc_auc =  round(metrics.auc(fpr, tpr), 4)

# In kết quả
print(f"MAE: {mae}")
print(f"MSE: {mse}")
print(f"RMSE: {rmse}")
print(f"ROC-AUC: {roc_auc}")