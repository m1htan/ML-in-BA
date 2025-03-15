import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from imblearn.over_sampling import BorderlineSMOTE
from MLinBA.Final_MLinBA.Utils.FileUtil import FileUtil
from MLinBA.Final_MLinBA.Model.Prepare.Statistic import Statistic

import os
path = "/Users/minhtan/Documents/GitHub/MLinBA/Final_MLinBA/Dataset/train.csv"
if not os.path.exists(path):
    raise FileNotFoundError(f"Không tìm thấy file {path}")
df = pd.read_csv('/Users/minhtan/Documents/GitHub/MLinBA/Final_MLinBA/Dataset/train.csv')

X = df.drop('Response', axis=1)
y = df['Response']

class DataProcessor(Statistic):
    def __init__(self, filepath=None, test_size=0.2, sampling_strategy=0.5, random_state=42):
        super().__init__()
        self.filepath = filepath
        self.test_size = test_size
        self.sampling_strategy = sampling_strategy
        self.random_state = random_state
        self.scaler = StandardScaler()
        self.label_encoders = {}
        self.sm = BorderlineSMOTE(sampling_strategy=sampling_strategy, random_state=random_state)
        self.X_train = self.X_test = self.y_train = self.y_test = None
        self.trained_model = None
        self.df = df

    def load_data(self, filepath=None):
        """Tải dữ liệu từ file CSV hoặc Excel"""
        if filepath:
            self.filepath = filepath
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"Không tìm thấy file {self.filepath}")
        if self.filepath.endswith('.csv'):
            self.df = pd.read_csv(self.filepath)
        elif self.filepath.endswith('.xlsx'):
            self.df = pd.read_excel(self.filepath)
        else:
            raise ValueError("Định dạng file không hỗ trợ")

    def preprocess(self):
        """Tiền xử lý dữ liệu: mã hóa và ánh xạ"""
        if self.df is None:
            raise ValueError("Dữ liệu chưa được tải. Gọi load_data() trước.")

        # Ánh xạ các categorical features
        self.df['Vehicle_Damage'] = self.df['Vehicle_Damage'].map({'Yes': 1, 'No': 0})
        self.df['Gender'] = self.df['Gender'].map({'Male': 0, 'Female': 1})
        vehicle_age_map = {'< 1 Year': 0, '1-2 Year': 1, '> 2 Years': 2}
        self.df['Vehicle_Age'] = self.df['Vehicle_Age'].map(vehicle_age_map)

        # Label encoding cho các cột khác
        for col in ['Region_Code', 'Policy_Sales_Channel']:
            le = LabelEncoder()
            self.df[col] = le.fit_transform(self.df[col])
            self.label_encoders[col] = le

        # Chuẩn hóa dữ liệu
        self.df[['Age', 'Annual_Premium', 'Vintage']] = self.scaler.fit_transform(
            self.df[['Age', 'Annual_Premium', 'Vintage']]
        )

    def prepare_data(self, test_size=None):
        """Chia dữ liệu và cân bằng bằng BorderlineSMOTE"""
        if self.df is None:
            raise ValueError("Dữ liệu chưa được tiền xử lý. Gọi preprocess() trước.")

        X = self.df.drop('Response', axis=1)
        y = self.df['Response']

        test_size = test_size if test_size is not None else self.test_size

        # Chia tập train-test
        X_train, X_test, y_train, y_test = train_test_split(
            X, y,
            test_size=test_size,
            stratify=y,
            random_state=self.random_state,
        )

        # **Lưu lại dữ liệu gốc trước khi áp dụng SMOTE**
        self.X_train, self.y_train = X_train, y_train  # Giữ lại dữ liệu train gốc

        # **Áp dụng BorderlineSMOTE để cân bằng dữ liệu**
        self.X_train_os, self.y_train_os = self.sm.fit_resample(X_train, y_train)

        # Lưu tập test
        self.X_test, self.y_test = X_test, y_test

    def get_data(self):
        """Trả về dữ liệu đã xử lý"""
        if self.X_train is None:
            raise ValueError("Dữ liệu chưa sẵn sàng. Gọi prepare_data() trước.")
        return self.X_train, self.X_test, self.y_train, self.y_test

    def transform_input(self, X_input):
        """Chuẩn hóa dữ liệu đầu vào mới"""
        return self.scaler.transform([X_input])

    def saveModel(self, filename):
        """Lưu model đã train"""
        if self.trained_model is None:
            raise ValueError("Không có model để lưu")
        return FileUtil.saveModel(self.trained_model, filename)

    def loadModel(self, filename):
        """Tải model đã lưu"""
        self.trained_model = FileUtil.loadModel(filename)
        return self.trained_model
