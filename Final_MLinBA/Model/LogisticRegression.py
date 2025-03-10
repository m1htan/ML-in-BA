import pickle
import numpy as np
from imblearn.over_sampling import BorderlineSMOTE
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from MLinBA.Final_MLinBA.Dataset.PrepareData import X, y

# Chia tập train-test với stratify
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# Thử Borderline-SMOTE thay vì SMOTE chuẩn
sm = BorderlineSMOTE(sampling_strategy=0.5, random_state=42)
X_train_os, y_train_os = sm.fit_resample(X_train, y_train)

# Chuẩn hóa dữ liệu
scaler = StandardScaler()
X_train_os = scaler.fit_transform(X_train_os)
X_test = scaler.transform(X_test)  # Chỉ transform tập test, không fit lại!

# Huấn luyện mô hình
model = LogisticRegression(C=0.1, solver='liblinear', max_iter=500)
model.fit(X_train_os, y_train_os)

# Dự đoán và đánh giá
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

class LogisticRegressionModel:
    def __init__(self, C=0.1, solver='liblinear', max_iter=500, sampling_strategy=0.5, random_state=42):
        self.scaler = StandardScaler()
        self.sm = BorderlineSMOTE(sampling_strategy=sampling_strategy, random_state=random_state)
        self.model = LogisticRegression(C=C, solver=solver, max_iter=max_iter, random_state=random_state)
        self.X_train = self.X_test = self.y_train = self.y_test = None

    def prepare_data(self, X, y, test_size=0.2):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, stratify=y, random_state=42)
        X_train_os, y_train_os = self.sm.fit_resample(X_train, y_train)
        self.X_train = self.scaler.fit_transform(X_train_os)
        self.X_test = self.scaler.transform(X_test)
        self.y_train, self.y_test = y_train_os, y_test

    def train(self):
        if self.X_train is None or self.y_train is None:
            raise ValueError("Data not prepared. Call prepare_data() before training.")
        self.model.fit(self.X_train, self.y_train)

    def evaluate(self):
        y_pred = self.model.predict(self.X_test)
        return classification_report(self.y_test, y_pred)

    def predict(self, X_input):
        X_input = np.array(X_input).reshape(1, -1)
        if X_input.shape[1] != self.X_train.shape[1]:
            raise ValueError(f"Expected {self.X_train.shape[1]} features, but got {X_input.shape[1]}")
        X_input_scaled = self.scaler.transform(X_input)
        return self.model.predict(X_input_scaled)[0]

    def predict_batch(self, X_inputs):
        X_inputs = np.array(X_inputs)
        if X_inputs.shape[1] != self.X_train.shape[1]:
            raise ValueError(f"Expected {self.X_train.shape[1]} features, but got {X_inputs.shape[1]}")
        X_inputs_scaled = self.scaler.transform(X_inputs)
        return self.model.predict(X_inputs_scaled)

    def save_model(self, file_path):
        with open(file_path, 'wb') as f:
            pickle.dump({
                'scaler': self.scaler,
                'model': self.model,
                'sampling_strategy': self.sm.sampling_strategy
            }, f)

    def load_model(self, file_path):
        with open(file_path, 'rb') as f:
            data = pickle.load(f)
            self.scaler = data['scaler']
            self.model = data['model']
            self.sm = BorderlineSMOTE(sampling_strategy=data.get('sampling_strategy', 0.5), random_state=42)
