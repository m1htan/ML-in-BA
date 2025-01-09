from K22416C.Ôn_tập_OOP.product import Product
from K22416C.Ôn_tập_OOP.filefactory import FileFactory
ff = FileFactory()
dataset = ff.readData("mydataset.json", Product)

# 1. Viết hàm lọc ra các sản phẩm có giá từ a tới b
def filter_products_by_price(dataset, a, b):
    return [product for product in dataset if a <= product.price <= b]

# Sử dụng hàm lọc
a = float(input("Nhập giá tối thiểu: "))
b = float(input("Nhập giá tối đa: "))
filtered_products = filter_products_by_price(dataset, a, b)

print(f"Danh sách sản phẩm có giá từ {a} tới {b}:")
for product in filtered_products:
    print(product)

# 2. Xoá tất cả các sản phẩm có giá nhỏ hơn x
def remove_products_below_price(dataset, x):
    return [product for product in dataset if product.price >= x]

# Sử dụng hàm xóa
x = float(input("Nhập giá tối thiểu để giữ lại sản phẩm: "))
dataset = remove_products_below_price(dataset, x)

print(f"Danh sách sản phẩm sau khi xóa các sản phẩm có giá nhỏ hơn {x}:")
for product in dataset:
    print(product)
