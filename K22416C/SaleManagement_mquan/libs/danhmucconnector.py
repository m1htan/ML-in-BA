from K22416C.SaleManagement_mquan.libs.connector import MySqlConnector
from K22416C.SaleManagement_mquan.models.danhmuc import DanhMuc


class DanhMucConnector(MySqlConnector):
    def LayToanBoDanhMuc(self):
        cursor = self.conn.cursor()
        sql = "select * from danhmuc"
        cursor.execute(sql)
        dataset = cursor.fetchall()
        dsdm = []
        for item in dataset:
            dsdm.append(DanhMuc(item[0],item[1],item[2]))
        cursor.close()
        return dsdm
