from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from MLinBA.Final_MLinBA.Model.LogisticRegression import X, y, X_test, y_test, X_train_os, y_train_os


dt_os_model = DecisionTreeClassifier(random_state=42)
dt_os_model.fit(X_train_os, y_train_os)
dt_os_pred = dt_os_model.predict(X_test)
print(classification_report(y_test, dt_os_pred))