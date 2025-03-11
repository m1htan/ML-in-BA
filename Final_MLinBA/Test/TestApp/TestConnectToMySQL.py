import mysql.connector

server="localhost"
port=3306
database="Final_MLinBA"
username="root"
password="Minhtan0410@"

conn = mysql.connector.connect(
                host=server,
                port=port,
                database=database,
                user=username,
                password=password)

cursor = conn.cursor()

sql="SELECT * FROM mhehe LIMIT 10;"
cursor.execute(sql)

dataset=cursor.fetchall()
align='{0:<3} {1:<6} {2:<15}'
print(align.format('ID', 'Gender','Age'))
for item in dataset:
    id=item[0]
    gender=item[1]
    age=item[2]
    print(align.format(id,gender,age))

cursor.close()