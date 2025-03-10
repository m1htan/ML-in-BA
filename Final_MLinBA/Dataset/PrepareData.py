import pandas as pd
import numpy as np
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split

df = pd.read_csv('/Users/minhtan/Documents/GitHub/MLinBA/Final_MLinBA/Dataset/train.csv')

X = df.drop('Response', axis=1)
y = df['Response']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)

sm = SMOTE()
X_train_os, y_train_os = sm.fit_resample(X_train, y_train)
