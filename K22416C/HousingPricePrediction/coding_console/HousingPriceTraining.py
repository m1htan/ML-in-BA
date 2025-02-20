import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import pickle


df = pd.read_csv('../dataset/USA_Housing.csv')
print(df.head())

# print(df.info())
# print(df.describe())
# sns.heatmap(df.corr())
# print(df.columns)

X = df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms','Avg. Area Number of Bedrooms', 'Area Population']]
y = df['Price']

# Chia tập dữ liệu ra làm 2: train và test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101)

# Tạo và train mô hình
lm = LinearRegression()
lm.fit(X_train,y_train)

# Sử dụng mô hình
predictions = lm.predict(X_test)
print("Kết quả dự đoán 20%: ")
print(predictions)

pre1 = lm.predict(X_test.iloc[[0]])
print("kết quả pre1=",pre1)

pre2=lm.predict([[66774.995817,5.717143,7.795215,4.320000,36788.980327]])
print("kết quả 2 =",pre2)

# print the intercept
print(lm.intercept_)
coeff_df = pd.DataFrame(lm.coef_,X.columns,columns=['Coefficient'])
print(coeff_df)

# Chỉ số đánh giá
print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))

modelname="../TrainedModel/housingmodel.zip"
pickle.dump(lm, open(modelname, 'wb'))