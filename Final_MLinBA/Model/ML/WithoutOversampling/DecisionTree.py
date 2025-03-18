import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix, mean_absolute_error, mean_squared_error, \
    roc_auc_score
import seaborn as sns
import matplotlib.pyplot as plt

from MLinBA.Final_MLinBA.Model.Prepare.PrepareData import DataProcessor


class DecisionTreeModel(DataProcessor):
    def __init__(self, random_state_dt=None):
        super().__init__()
        self.prepare_data()
        self.model = DecisionTreeClassifier(random_state=random_state_dt)

    def train(self):
        self.model.fit(self.X_train, self.y_train)
        self.trained_model = self.model

    def evaluate(self):
        X_test, y_test = self.X_test, self.y_test

        y_pred = self.model.predict(X_test)
        y_probs = self.model.predict_proba(X_test)[:, 1]  # Lấy xác suất của lớp 1

        print(classification_report(y_test, y_pred))

        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        roc_auc = roc_auc_score(y_test, y_probs)

        # Trả về kết quả dưới dạng dictionary
        return {
            "MAE": mae,
            "MSE": mse,
            "RMSE": rmse,
            "ROC_SCORE": roc_auc
        }