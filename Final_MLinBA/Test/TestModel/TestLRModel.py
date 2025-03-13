import unittest
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score, mean_absolute_error, mean_squared_error

from MLinBA.Final_MLinBA.Model.Prepare.PrepareData import X, y, DataProcessor


class TestLogisticModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Chuẩn bị dữ liệu và huấn luyện mô hình trước khi chạy test"""
        # Khởi tạo đối tượng DataProcessor
        cls.processor = DataProcessor()

        # Chuẩn bị dữ liệu
        cls.processor.prepare_data(X, y)

        # Huấn luyện mô hình Logistic Regression
        cls.processor.model = LogisticRegression(C=0.1, solver='liblinear', max_iter=500)
        cls.processor.model.fit(cls.processor.X_train, cls.processor.y_train)

    def test_prediction_shape(self):
        """Kiểm tra kích thước đầu ra của y_pred"""
        y_pred = self.processor.predict(self.processor.X_test)
        self.assertEqual(len(y_pred), len(self.processor.y_test), "Số lượng dự đoán không khớp với số mẫu test")

    def test_classification_report(self):
        """Kiểm tra xem classification_report có thể chạy mà không lỗi"""
        y_pred = self.processor.predict(self.processor.X_test)
        report = classification_report(self.processor.y_test, y_pred)
        self.assertIsInstance(report, str, "Classification report không phải là chuỗi")

    def test_performance_metrics(self):
        """Kiểm tra các chỉ số đánh giá"""
        y_pred = self.processor.predict(self.processor.X_test)
        y_probs = self.processor.model.predict_proba(self.processor.X_test)[:, 1]  # Xác suất lớp 1

        # Tính toán các chỉ số
        mae = mean_absolute_error(self.processor.y_test, y_pred)
        mse = mean_squared_error(self.processor.y_test, y_pred)
        rmse = np.sqrt(mse)
        roc_auc = roc_auc_score(self.processor.y_test, y_probs)

        # Kiểm tra giá trị hợp lệ
        self.assertGreaterEqual(mae, 0, "MAE không hợp lệ")
        self.assertGreaterEqual(mse, 0, "MSE không hợp lệ")
        self.assertGreaterEqual(rmse, 0, "RMSE không hợp lệ")
        self.assertGreaterEqual(roc_auc, 0, "ROC-AUC không hợp lệ")
        self.assertLessEqual(roc_auc, 1, "ROC-AUC không thể lớn hơn 1")

    def test_save_model(self):
        """Kiểm tra việc lưu mô hình"""
        # Lưu mô hình
        ret = self.processor.saveModel("/Users/minhtan/Documents/GitHub/MLinBA/Final_MLinBA/Assets/WithOversampling/LogisticRegression_model.zip")
        self.assertTrue(ret, "Lưu mô hình không thành công")
