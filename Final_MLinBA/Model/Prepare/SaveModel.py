import unittest
import numpy as np
from sklearn.metrics import classification_report, roc_auc_score, mean_absolute_error, mean_squared_error

from MLinBA.Final_MLinBA.Model.ML.WithOversampling.DecisionTree import DecisionTreeModelOversampling
from MLinBA.Final_MLinBA.Model.ML.WithOversampling.LogisticRegression import LogisticRegressionModelOversampling
from MLinBA.Final_MLinBA.Model.ML.WithOversampling.RandomForest import RandomForestModelOversampling
from MLinBA.Final_MLinBA.Model.ML.WithOversampling.XGBoost import XGBoostModelOversampling

from MLinBA.Final_MLinBA.Model.ML.WithoutOversampling.DecisionTree import DecisionTreeModel
from MLinBA.Final_MLinBA.Model.ML.WithoutOversampling.LogisticRegression import LogisticRegressionModel
from MLinBA.Final_MLinBA.Model.ML.WithoutOversampling.RandomForest import RandomForestModel
from MLinBA.Final_MLinBA.Model.ML.WithoutOversampling.XGBoost import XGBoostModel


class TestLogisticModel_LG_O(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.processor = LogisticRegressionModelOversampling()
        cls.processor.prepare_data()
        cls.processor.train()

    def test_prediction_shape(self):
        """Kiểm tra kích thước đầu ra của y_pred"""
        y_pred = self.processor.model.predict(self.processor.X_test)
        self.assertEqual(len(y_pred), len(self.processor.y_test), "Số lượng dự đoán không khớp với số mẫu test")

    def test_classification_report(self):
        """Kiểm tra xem classification_report có thể chạy mà không lỗi"""
        y_pred = self.processor.model.predict(self.processor.X_test)
        report = classification_report(self.processor.y_test, y_pred)
        self.assertIsInstance(report, str, "Classification report không phải là chuỗi")

    def test_performance_metrics(self):
        """Kiểm tra các chỉ số đánh giá"""
        y_pred = self.processor.model.predict(self.processor.X_test)
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
        if self.processor.model is None:
            self.fail("Mô hình chưa được khởi tạo hoặc chưa được huấn luyện")

        ret = self.processor.saveModel("/Users/minhtan/Documents/GitHub/MLinBA/Final_MLinBA/Assets/WithOversampling/LogisticRegressionModelOversampling_model.zip")
        self.assertTrue(ret, "Lưu mô hình không thành công")

class TestLogisticModel_DT_O(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.processor = DecisionTreeModelOversampling()
        cls.processor.prepare_data()
        cls.processor.train()

    def test_prediction_shape(self):
        """Kiểm tra kích thước đầu ra của y_pred"""
        y_pred = self.processor.model.predict(self.processor.X_test)
        self.assertEqual(len(y_pred), len(self.processor.y_test), "Số lượng dự đoán không khớp với số mẫu test")

    def test_classification_report(self):
        """Kiểm tra xem classification_report có thể chạy mà không lỗi"""
        y_pred = self.processor.model.predict(self.processor.X_test)
        report = classification_report(self.processor.y_test, y_pred)
        self.assertIsInstance(report, str, "Classification report không phải là chuỗi")

    def test_performance_metrics(self):
        """Kiểm tra các chỉ số đánh giá"""
        y_pred = self.processor.model.predict(self.processor.X_test)
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
        if self.processor.model is None:
            self.fail("Mô hình chưa được khởi tạo hoặc chưa được huấn luyện")

        ret = self.processor.saveModel("/Users/minhtan/Documents/GitHub/MLinBA/Final_MLinBA/Assets/WithOversampling/DecisionTreeModelOversampling_model.zip")
        self.assertTrue(ret, "Lưu mô hình không thành công")

class TestLogisticModel_RF_O(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.processor = RandomForestModelOversampling()
        cls.processor.prepare_data()
        cls.processor.train()

    def test_prediction_shape(self):
        """Kiểm tra kích thước đầu ra của y_pred"""
        y_pred = self.processor.model.predict(self.processor.X_test)
        self.assertEqual(len(y_pred), len(self.processor.y_test), "Số lượng dự đoán không khớp với số mẫu test")

    def test_classification_report(self):
        """Kiểm tra xem classification_report có thể chạy mà không lỗi"""
        y_pred = self.processor.model.predict(self.processor.X_test)
        report = classification_report(self.processor.y_test, y_pred)
        self.assertIsInstance(report, str, "Classification report không phải là chuỗi")

    def test_performance_metrics(self):
        """Kiểm tra các chỉ số đánh giá"""
        y_pred = self.processor.model.predict(self.processor.X_test)
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
        if self.processor.model is None:
            self.fail("Mô hình chưa được khởi tạo hoặc chưa được huấn luyện")

        ret = self.processor.saveModel("/Users/minhtan/Documents/GitHub/MLinBA/Final_MLinBA/Assets/WithOversampling/RandomForestModelOversampling_model.zip")
        self.assertTrue(ret, "Lưu mô hình không thành công")

class TestLogisticModel_XG_O(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.processor = XGBoostModelOversampling()
        cls.processor.prepare_data()
        cls.processor.train()

    def test_prediction_shape(self):
        """Kiểm tra kích thước đầu ra của y_pred"""
        y_pred = self.processor.model.predict(self.processor.X_test)
        self.assertEqual(len(y_pred), len(self.processor.y_test), "Số lượng dự đoán không khớp với số mẫu test")

    def test_classification_report(self):
        """Kiểm tra xem classification_report có thể chạy mà không lỗi"""
        y_pred = self.processor.model.predict(self.processor.X_test)
        report = classification_report(self.processor.y_test, y_pred)
        self.assertIsInstance(report, str, "Classification report không phải là chuỗi")

    def test_performance_metrics(self):
        """Kiểm tra các chỉ số đánh giá"""
        y_pred = self.processor.model.predict(self.processor.X_test)
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
        if self.processor.model is None:
            self.fail("Mô hình chưa được khởi tạo hoặc chưa được huấn luyện")

        ret = self.processor.saveModel("/Users/minhtan/Documents/GitHub/MLinBA/Final_MLinBA/Assets/WithOversampling/XGBoostModelOversampling_model.zip")
        self.assertTrue(ret, "Lưu mô hình không thành công")



class TestLogisticModel_DT(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.processor = DecisionTreeModel()
        cls.processor.prepare_data()
        cls.processor.train()

    def test_prediction_shape(self):
        """Kiểm tra kích thước đầu ra của y_pred"""
        y_pred = self.processor.model.predict(self.processor.X_test)
        self.assertEqual(len(y_pred), len(self.processor.y_test), "Số lượng dự đoán không khớp với số mẫu test")

    def test_classification_report(self):
        """Kiểm tra xem classification_report có thể chạy mà không lỗi"""
        y_pred = self.processor.model.predict(self.processor.X_test)
        report = classification_report(self.processor.y_test, y_pred)
        self.assertIsInstance(report, str, "Classification report không phải là chuỗi")

    def test_performance_metrics(self):
        """Kiểm tra các chỉ số đánh giá"""
        y_pred = self.processor.model.predict(self.processor.X_test)
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
        if self.processor.model is None:
            self.fail("Mô hình chưa được khởi tạo hoặc chưa được huấn luyện")

        ret = self.processor.saveModel("/Users/minhtan/Documents/GitHub/MLinBA/Final_MLinBA/Assets/WithoutOversampling/DecisionTreeModel_model.zip")
        self.assertTrue(ret, "Lưu mô hình không thành công")

class TestLogisticModel_LG(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.processor = LogisticRegressionModel()
        cls.processor.prepare_data()
        cls.processor.train()

    def test_prediction_shape(self):
        """Kiểm tra kích thước đầu ra của y_pred"""
        y_pred = self.processor.model.predict(self.processor.X_test)
        self.assertEqual(len(y_pred), len(self.processor.y_test), "Số lượng dự đoán không khớp với số mẫu test")

    def test_classification_report(self):
        """Kiểm tra xem classification_report có thể chạy mà không lỗi"""
        y_pred = self.processor.model.predict(self.processor.X_test)
        report = classification_report(self.processor.y_test, y_pred)
        self.assertIsInstance(report, str, "Classification report không phải là chuỗi")

    def test_performance_metrics(self):
        """Kiểm tra các chỉ số đánh giá"""
        y_pred = self.processor.model.predict(self.processor.X_test)
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
        if self.processor.model is None:
            self.fail("Mô hình chưa được khởi tạo hoặc chưa được huấn luyện")

        ret = self.processor.saveModel("/Users/minhtan/Documents/GitHub/MLinBA/Final_MLinBA/Assets/WithoutOversampling/LogisticRegressionModel_model.zip")
        self.assertTrue(ret, "Lưu mô hình không thành công")

class TestLogisticModel_RF(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.processor = RandomForestModel()
        cls.processor.prepare_data()
        cls.processor.train()

    def test_prediction_shape(self):
        """Kiểm tra kích thước đầu ra của y_pred"""
        y_pred = self.processor.model.predict(self.processor.X_test)
        self.assertEqual(len(y_pred), len(self.processor.y_test), "Số lượng dự đoán không khớp với số mẫu test")

    def test_classification_report(self):
        """Kiểm tra xem classification_report có thể chạy mà không lỗi"""
        y_pred = self.processor.model.predict(self.processor.X_test)
        report = classification_report(self.processor.y_test, y_pred)
        self.assertIsInstance(report, str, "Classification report không phải là chuỗi")

    def test_performance_metrics(self):
        """Kiểm tra các chỉ số đánh giá"""
        y_pred = self.processor.model.predict(self.processor.X_test)
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
        if self.processor.model is None:
            self.fail("Mô hình chưa được khởi tạo hoặc chưa được huấn luyện")

        ret = self.processor.saveModel("/Users/minhtan/Documents/GitHub/MLinBA/Final_MLinBA/Assets/WithoutOversampling/RandomForestModel_model.zip")
        self.assertTrue(ret, "Lưu mô hình không thành công")

class TestLogisticModel_XG(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.processor = XGBoostModel()
        cls.processor.prepare_data()
        cls.processor.train()

    def test_prediction_shape(self):
        """Kiểm tra kích thước đầu ra của y_pred"""
        y_pred = self.processor.model.predict(self.processor.X_test)
        self.assertEqual(len(y_pred), len(self.processor.y_test), "Số lượng dự đoán không khớp với số mẫu test")

    def test_classification_report(self):
        """Kiểm tra xem classification_report có thể chạy mà không lỗi"""
        y_pred = self.processor.model.predict(self.processor.X_test)
        report = classification_report(self.processor.y_test, y_pred)
        self.assertIsInstance(report, str, "Classification report không phải là chuỗi")

    def test_performance_metrics(self):
        """Kiểm tra các chỉ số đánh giá"""
        y_pred = self.processor.model.predict(self.processor.X_test)
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
        if self.processor.model is None:
            self.fail("Mô hình chưa được khởi tạo hoặc chưa được huấn luyện")

        ret = self.processor.saveModel("/Users/minhtan/Documents/GitHub/MLinBA/Final_MLinBA/Assets/WithoutOversampling/XGBoostModel_model.zip")
        self.assertTrue(ret, "Lưu mô hình không thành công")