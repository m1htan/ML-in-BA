import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import BorderlineSMOTE

from MLinBA.Final_MLinBA.Utils.FileUtil import FileUtil

import os
path = "/MLinBA/Final_MLinBA/Dataset/train.csv"
if not os.path.exists(path):
    raise FileNotFoundError(f"Không tìm thấy file {path}")
df = pd.read_csv('/MLinBA/Final_MLinBA/Dataset/train.csv')

X = df.drop('Response', axis=1)
y = df['Response']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)

sm = SMOTE()
X_train_os, y_train_os = sm.fit_resample(X_train, y_train)

class DataProcessor:
    def __init__(self, test_size=0.2, sampling_strategy=0.5, random_state=42):
        self.test_size = test_size
        self.sampling_strategy = sampling_strategy
        self.random_state = random_state
        self.scaler = StandardScaler()
        self.sm = BorderlineSMOTE(sampling_strategy=sampling_strategy, random_state=random_state)
        self.X_train = self.X_test = self.y_train = self.y_test = None
        self.model = None
        self.trainedmodel = None

    def prepare_data(self, X, y):
        # Chia dữ liệu train-test
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=self.test_size, stratify=y, random_state=self.random_state)
        # Áp dụng Borderline-SMOTE
        X_train_os, y_train_os = self.sm.fit_resample(X_train, y_train)
        # Chuẩn hóa dữ liệu
        self.X_train = self.scaler.fit_transform(X_train_os)
        self.X_test = self.scaler.transform(X_test)
        self.y_train, self.y_test = y_train_os, y_test

    def get_data(self):
        if self.X_train is None or self.y_train is None:
            raise ValueError("Data not prepared. Call prepare_data() first.")
        return self.X_train, self.X_test, self.y_train, self.y_test

    def transform_input(self, X_input):
        X_input_scaled = self.scaler.transform([X_input])
        return X_input_scaled

    def predict(self,columns_input):
        pred = self.model.predict(columns_input)
        return pred

    def saveModel(self,fileName):
        ret=FileUtil.saveModel(self.trainedmodel,fileName)
        return ret

    def loadModel(self,fileName):
        self.trainedmodel=FileUtil.loadModel(fileName)
        self.scaler.fit_transform(self.trainedmodel.X_train)
        self.model=self.trainedmodel.model
        return self.model