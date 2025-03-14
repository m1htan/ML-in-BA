import unittest

from MLinBA.Final_MLinBA.Model.ML.WithOversampling.LogisticRegression import LogisticRegressionModel

class TestLoadModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.processor = LogisticRegressionModel()
        cls.model = LogisticRegressionModel()

    def test_save_and_load_model(self):
        # Tải mô hình
        self.processor.loadModel("/Users/minhtan/Documents/GitHub/MLinBA/Final_MLinBA/Assets/WithOversampling/LogisticRegression_model.zip")
        self.assertIsNotNone(self.processor.model, "Tải mô hình không thành công")