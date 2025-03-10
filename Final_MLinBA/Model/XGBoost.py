import xgboost as xgb
from sklearn.metrics import confusion_matrix, classification_report
from MLinBA.Final_MLinBA.Model.LogisticRegression import X, y, X_test, y_test, X_train_os, y_train_os

model_xgb = xgb.XGBClassifier(random_state=42, n_estimators=100)
model_xgb.fit(X_train_os, y_train_os)
y_os_pred = model_xgb.predict(X_test)
print(classification_report(y_test, y_os_pred))
