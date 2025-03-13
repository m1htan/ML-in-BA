class MetricsResult:
    def __init__(self,mae,mse,rmse,roc):
        self.MAE=mae
        self.MSE=mse
        self.RMSE=rmse
        self.ROC=roc

    def __str__(self):
        result="MAE=%s"%self.MAE+"\n"+"MSE=%s"%self.MSE+"\n"+"RMSE=%s"%self.RMSE+"\n"+"ROC-AUC Score=%s"%self.ROC+"\n"
        return result