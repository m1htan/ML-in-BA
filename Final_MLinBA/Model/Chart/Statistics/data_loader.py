# data_loader.py
import pandas as pd

df = pd.read_csv('/Users/minhtan/Documents/GitHub/MLinBA/Final_MLinBA/Dataset/train.csv')

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = df
        self.load_data()

    def load_data(self):
        try:
            self.df = pd.read_csv(self.file_path)
            print(f"Đã tải dữ liệu từ {self.file_path} thành công!")
            self.map_original_labels()
        except Exception as e:
            print(f"Lỗi khi tải dữ liệu: {e}")
            self.df = pd.DataFrame()

    def map_original_labels(self):
        if 'Gender' in self.df.columns:
            self.df['Gender'] = self.df['Gender'].map({0: 'Male', 1: 'Female'}).fillna(self.df['Gender'])
        if 'Vehicle_Damage' in self.df.columns:
            self.df['Vehicle_Damage'] = self.df['Vehicle_Damage'].map({0: 'No', 1: 'Yes'}).fillna(self.df['Vehicle_Damage'])
        if 'Vehicle_Age' in self.df.columns:
            self.df['Vehicle_Age'] = self.df['Vehicle_Age'].replace({
                0: '< 1 Year',
                1: '1-2 Year',
                2: '> 2 Years'
            })

    def get_data(self):
        return self.df