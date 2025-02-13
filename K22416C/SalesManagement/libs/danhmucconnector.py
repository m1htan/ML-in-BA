from K22416C.SalesManagement.libs.connector import MySQLConnector
from K22416C.SalesManagement.models.danhmuc import DanhMuc


class DanhMucConnector(MySQLConnector):
    def LayToanBoDanhMuc(self):
        cursor = self.conn.cursor()
        sql="select * from DANHMUC"
        cursor.execute(sql)
        dataset=cursor.fetchone()
        dsdm=[]
        for item in dataset:
            id=item[0]
            ma=item[1]
            ten=item[2]
            dsdm.append(DanhMuc(item[0], item[1], item[2]))
        cursor.close()
        return dsdm



