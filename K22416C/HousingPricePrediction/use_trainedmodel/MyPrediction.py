import pickle

modelname=("../TrainedModel/housingmodel"
           ".zip")
trainedmodel=pickle.load(open(modelname, 'rb'))
prediction=trainedmodel.predict([[66774.995817,5.717143,7.795215,4.320000,36788.980327]])
print("kết quả =",prediction)