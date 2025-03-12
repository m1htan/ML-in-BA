import xgboost as xgb
from sklearn.metrics import classification_report
from sklearn import metrics
import numpy as np

from MLinBA.Final_MLinBA.Dataset.PrepareData import X_train_os, y_train_os, X_test, y_test
from MLinBA.Final_MLinBA.Model.ML.LogisticRegression import y_pred

model_xgb = xgb.XGBClassifier(random_state=42, n_estimators=100)
model_xgb.fit(X_train_os, y_train_os)
y_os_pred = model_xgb.predict(X_test)
print(classification_report(y_test, y_os_pred))

# ĐÁNH GIÁ MODEL
# Dự đoán xác suất
y_prob = model_xgb.predict_proba(X_test)[:, 1]  # Xác suất thuộc lớp dương

# Tính các chỉ số hồi quy
mae = metrics.mean_absolute_error(y_test, y_pred)
mse = metrics.mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

# Tính điểm ROC-AUC
fpr, tpr, _ = metrics.roc_curve(y_test, y_prob)
roc_auc = metrics.auc(fpr, tpr)

# In kết quả
print(f'MAE: {mae:.4f}')
print(f'MSE: {mse:.4f}')
print(f'RMSE: {rmse:.4f}')
print(f'ROC-AUC Score: {roc_auc:.4f}')