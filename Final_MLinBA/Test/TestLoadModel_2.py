# from MLinBA.Final_MLinBA.Model.ML.LogisticRegression import LogisticRegressionModel
from sklearn.linear_model import LogisticRegression

from MLinBA.Final_MLinBA.Model.ML.WithOversampling.LogisticRegression import LogisticRegressionModel


pm=LogisticRegressionModel()
pm.loadModel("../Assets/TrainedModel_GenderAgePayment.zip")
