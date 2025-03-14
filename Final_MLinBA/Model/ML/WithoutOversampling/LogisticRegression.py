from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

from MLinBA.Final_MLinBA.Model.Prepare.PrepareData import DataProcessor


class LogisticRegressionModel(DataProcessor):
    def __init__(self, C=0.1, max_iter=500):
        super().__init__()
        self.prepare_data()
        self.model = LogisticRegression(C=C, max_iter=max_iter)

    def train(self):
        self.model.fit(self.X_train, self.y_train)
        self.trained_model = self.model

    def evaluate(self, X_test, y_test):
        y_pred = self.model.predict(X_test)
        print(classification_report(y_test, y_pred))

        cm = confusion_matrix(y_test, y_pred)

        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
        plt.xlabel("Predicted Label")
        plt.ylabel("True Label")
        plt.title("Confusion Matrix - Logistic Regression")
        plt.show()
