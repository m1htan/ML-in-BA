from K22416C.SAKILA_BAITAP.Connectors.Connector_Flask import getConnect, queryDataset

conn = getConnect('localhost', 3306, 'sakila', 'root', 'Minhtan0410@')

sql1 = "select * from customer"
sql2 = "select * from inventory"
sql3 = "select * from rental"
sql4 = "select * from film"

df1 = queryDataset(conn, sql1)
df2 = queryDataset(conn, sql2)
df3 = queryDataset(conn, sql3)
df4 = queryDataset(conn, sql4)

print(df1)
print(df2)
print(df3)
print(df4)


print(df1.columns)  # Kiểm tra bảng Customer
print(df3.columns)  # Kiểm tra bảng Rental
