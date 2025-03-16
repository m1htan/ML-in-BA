import pandas as pd
import self

df = pd.read_csv('/Users/minhtan/Documents/GitHub/MLinBA/Final_MLinBA/Dataset/train.csv')

print(df.columns)

print(df['Vehicle_Age'].unique())

print("📌 Giá trị gốc của Vehicle_Age:", df['Vehicle_Age'].unique())
print("📌 Tổng số dòng NaN:", df['Vehicle_Age'].isna().sum())

print(df['Region_Code'].value_counts())  # Kiểm tra dữ liệu đầu vào

