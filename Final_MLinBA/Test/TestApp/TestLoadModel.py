# from MLinBA.Final_MLinBA.Model.ML.LogisticRegression import LogisticRegressionModel
from sklearn.linear_model import LogisticRegression

pm=LogisticRegressionModel()
pm.loadModel("../Assets/TrainedModel_GenderAgePayment.zip")

gender="Female"
age=61
payment="Cash"
pred=pm.predictPriceFromGenderAndAgeAndPayment(gender,age,payment)
print("Gender=%s and Age=%s and payment=%s=>Price=%s"%(gender,age,payment,pred))
#Gender=Female and Age=61 and payment=Cash=>Price=[692.98688316]