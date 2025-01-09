from K22416C.Ôn_tập_OOP.product import Product
from K22416C.Ôn_tập_OOP.filefactory import FileFactory

ff = FileFactory()
dataset = ff.readData("mydataset.json", Product)
print("Danh sách sản phẩm: ")
for product in dataset:
    print(product)
