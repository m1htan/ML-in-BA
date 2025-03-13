import unittest

from MLinBA.Final_MLinBA.Model.Prepare.PrepareData import DataProcessor

class TestLoadModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.processor = DataProcessor()
    def test_save_and_load_model(self):
        # Tải mô hình
        self.processor.loadModel("/Users/minhtan/Documents/GitHub/MLinBA/Final_MLinBA/Assets/WithOversampling/LogisticRegression_model.zip")
        self.assertIsNotNone(self.processor.model, "Tải mô hình không thành công")