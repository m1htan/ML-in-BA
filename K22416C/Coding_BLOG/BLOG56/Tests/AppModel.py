from K22416C.Coding_BLOG.BLOG56.Connectors.Connector import Connector
from K22416C.Coding_BLOG.BLOG56.Models.PurchaseMLModel import PurchaseMLModel

connector=Connector(server="localhost",port=3306,database="lecturer_retails",username="root",password="Minhtan0410@")
connector.connect()
pm=PurchaseMLModel(connector)
pm.execPurchaseHistory()

dfTransform=pm.processTransform()
print(dfTransform.head())
pm.buildCorrelationMatrix(dfTransform)