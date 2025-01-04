## Slide 7: Lọc dữ liệu thiếu
from numpy import nan as NA
import pandas as pd
data = pd.DataFrame([[1., 6.5, 3.],
                     [1., NA, NA],
                     [NA, NA, NA],
                     [NA, 6.5, 3.]])
print(data)
print("-"*10)

cleaned = data.dropna() # Xóa hàng chứa bất kỳ giá trị thiếu nào.
print(cleaned)
print("-"*10)

cleaned2=data.dropna(how='all') # Xóa chỉ khi tất cả giá trị trong hàng đều bị thiếu.
print(cleaned2)
print("-"*10)

cleaned3 = data.dropna(subset=[1])  # Xóa hàng nếu cột thứ 1 có giá trị thiếu
print(cleaned3)
print("-"*10)

cleaned4 = data.dropna(axis=1)  # Xóa các cột có dữ liệu thiếu
print(cleaned4)
print("-"*10)

cleaned5 = data.dropna(thresh=2)  # Giữ hàng có ít nhất 2 giá trị không thiếu
print(cleaned5)
print("-"*10)

cleaned6 = data[data[0].notna()]  # Lọc các hàng mà cột đầu tiên không bị thiếu
print(cleaned6)
print("-"*10)

data_filled = data.fillna(0)  # Thay NA bằng 0
cleaned7 = data_filled[data_filled[0] != 0]  # Lọc giá trị không phải 0
print(cleaned7)
print("-"*10)

cleaned8 = data[data[1].isna()]  # Chỉ lấy các hàng mà cột thứ 1 bị thiếu
print(cleaned8)
print("-"*10)

cleaned9 = data[data[1] == 1]  # Lọc các hàng mà cột 1 không bị thiếu
print(cleaned9)
print("-"*10)

cleaned10=data.dropna(how='any')
print(cleaned10)
print("-"*10)