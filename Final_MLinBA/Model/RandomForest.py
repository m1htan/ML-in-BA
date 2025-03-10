from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from MLinBA.Final_MLinBA.Model.LogisticRegression import X, y, X_test, y_test, X_train_os, y_train_os

rf_os_model = RandomForestClassifier(random_state=42, n_estimators=100)
rf_os_model.fit(X_train_os, y_train_os)
rf_os_pred = rf_os_model.predict(X_test)
print(classification_report(y_test, rf_os_pred))