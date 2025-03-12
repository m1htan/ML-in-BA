from MLinBA.Final_MLinBA.Connectors.Connector import Connector
from MLinBA.Final_MLinBA.Model.Prepare.PreprocessingData import PreprocessingData

connector=Connector(server="localhost",port=3306,database="Final_MLinBA",username="root",password="Minhtan0410@")
connector.connect()
pm=PreprocessingData(connector)
pm.execPurchaseHistory()

dfTransform=pm.processTransform()
print(dfTransform.head())
pm.buildCorrelationMatrix(dfTransform)