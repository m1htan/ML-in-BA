class Product:
    def __init__(self,ProductId,ProductName,Price):
        self.ProductId=ProductId
        self.ProductName=ProductName
        self.Price=Price
    def __str__(self):
        return str(self.ProductId) +" - "+self.ProductName +"-"+str(self.Price)