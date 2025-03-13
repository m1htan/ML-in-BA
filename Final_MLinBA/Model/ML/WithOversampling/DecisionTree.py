import numpy as np
from sklearn import metrics
from sklearn.metrics import classification_report
from MLinBA.Final_MLinBA.Model.ML.WithOversampling.LogisticRegression import X_test, y_test, X_train_os, y_train_os, y_pred
from sklearn.tree import DecisionTreeClassifier


dt_os_model = DecisionTreeClassifier(random_state=42)
dt_os_model.fit(X_train_os, y_train_os)
dt_os_pred = dt_os_model.predict(X_test)
print(classification_report(y_test, dt_os_pred))

# Dự đoán xác suất
y_prob = dt_os_model.predict_proba(X_test)[:, 1]  # Xác suất thuộc lớp dương
