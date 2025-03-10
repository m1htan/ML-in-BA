from MLinBA.Final_MLinBA.Dataset.PrepareData import X, y
from MLinBA.Final_MLinBA.Model.LogisticRegression import LogisticRegressionModel

pm=LogisticRegressionModel()

# Khởi tạo mô hình
lr_model = LogisticRegressionModel()
lr_model.prepare_data(X, y)
lr_model.train()

# Đánh giá mô hình
eresult = lr_model.evaluate()
print("Evaluation Result:\n", eresult)

ret=pm.save_model("../Assets/LR_model.zip")
