import unittest
import numpy as np
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
from MLinBA.Final_MLinBA.Dataset.PrepareData import DataProcessor
from MLinBA.Final_MLinBA.Model.LogisticRegression import X, y


class TestRandomForestModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Chuẩn bị dữ liệu và huấn luyện mô hình trước khi chạy test"""
        # Khởi tạo đối tượng DataProcessor
        cls.processor = DataProcessor()

        # Chuẩn bị dữ liệu
        cls.processor.prepare_data(X, y)

        # Huấn luyện mô hình Random Forest
        cls.processor.model = RandomForestClassifier(random_state=42, n_estimators=100)  # Khởi tạo mô hình
        cls.processor.model.fit(cls.processor.X_train, cls.processor.y_train)  # Huấn luyện mô hình

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
        y_prob = self.processor.model.predict_proba(self.processor.X_test)[:, 1]  # Xác suất thuộc lớp dương

        # Tính toán các chỉ số
        mae = metrics.mean_absolute_error(self.processor.y_test, y_pred)
        mse = metrics.mean_squared_error(self.processor.y_test, y_pred)
        rmse = np.sqrt(mse)
        fpr, tpr, _ = metrics.roc_curve(self.processor.y_test, y_prob)
        roc_auc = metrics.auc(fpr, tpr)

        # Kiểm tra giá trị hợp lệ
        self.assertGreaterEqual(mae, 0, "MAE không hợp lệ")
        self.assertGreaterEqual(mse, 0, "MSE không hợp lệ")
        self.assertGreaterEqual(rmse, 0, "RMSE không hợp lệ")
        self.assertGreaterEqual(roc_auc, 0, "ROC-AUC không hợp lệ")
        self.assertLessEqual(roc_auc, 1, "ROC-AUC không thể lớn hơn 1")

    def test_save_and_load_model(self):
        """Kiểm tra việc lưu và tải mô hình"""
        # Lưu mô hình
        ret = self.processor.saveModel("../Assets/RandomForest_model.zip")
        self.assertTrue(ret, "Lưu mô hình không thành công")
