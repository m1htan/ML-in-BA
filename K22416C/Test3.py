from sklearn.metrics import mean_squared_error
import numpy as np

y_true = np.array([3, -0.5, 2, 7])
y_pred = np.array([2.5, 0.0, 2, 8])

mse = mean_squared_error(y_true, y_pred)  # Nếu lỗi xảy ra, vấn đề có thể ở code của bạn
print("MSE:", mse)

print(mean_squared_error)
