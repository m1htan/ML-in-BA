class Product:
    def __init__(self, id=None, name=None, price=None):
        self.id=id
        self.name=name
        self.price=price
    def __str__(self):
        infor=f"{self.id}\t{self.name}\t{self.price}"
        return infor