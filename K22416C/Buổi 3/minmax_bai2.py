import pandas as pd

def find_orders_within_range(df, minValue, maxValue, sortType=True):
    # Tính tổng giá trị từng đơn hàng
    order_totals = df.groupby('OrderID').apply(lambda x: (x['UnitPrice'] * x['Quantity'] * (1 - x['Discount'])).sum())

    # Lọc các đơn hàng trong phạm vi [minValue, maxValue]
    orders_within_range = order_totals[(order_totals >= minValue) & (order_totals <= maxValue)]

    # Tạo DataFrame chứa mã hóa đơn và tổng giá trị
    result = orders_within_range.reset_index(name='TotalValue')

    # Sắp xếp danh sách theo giá trị TotalValue (tăng dần hoặc giảm dần)
    result = result.sort_values(by='TotalValue', ascending=sortType)

    return result

# Đọc dữ liệu từ file CSV
df = pd.read_csv("../Dataset/SalesTransactions.csv")

# Input từ người dùng
minValue = float(input("Nhập giá trị tối thiểu (minValue): "))
maxValue = float(input("Nhập giá trị tối đa (maxValue): "))
sortType = input("Sắp xếp tăng dần (True) hay giảm dần (False)? ").strip().lower() == 'true'

# Gọi hàm và in kết quả
result = find_orders_within_range(df, minValue, maxValue, sortType)
print('Danh sách các hóa đơn trong phạm vi giá trị từ', minValue, 'đến', maxValue, ' là:')
print(result)