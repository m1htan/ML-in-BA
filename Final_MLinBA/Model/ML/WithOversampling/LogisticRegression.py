from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

from MLinBA.Final_MLinBA.Model.Prepare.PrepareData import DataProcessor


class LogisticRegressionModel(DataProcessor):
    def train_LR(self, X_train_os, y_train_os, X_test, y_test, model):
        # Huấn luyện mô hình
        self.model = LogisticRegression(C=0.1, solver='liblinear', max_iter=500)
        self.model.fit(X_train_os, y_train_os)

    def predict_LR(self, model,X_test, y_test):
        # Dự đoán và đánh giá
        y_pred = model.predict(X_test)
        print(classification_report(y_test, y_pred))

        # Dự đoán xác suất
        y_probs = model.predict_proba(X_test)[:, 1]  # Xác suất của lớp dương (1)
