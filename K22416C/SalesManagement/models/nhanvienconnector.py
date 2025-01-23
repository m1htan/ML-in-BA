from SalesManagement.libs.connector import MySQLConnector
from SalesManagement.models.nhanvien import NhanVien


class NhanVienConnector(MySQLConnector):
    def dang_nhap(self, username, password):
        cursor=self.conn.cursor()
        sql='Select * from NHANVIEN where USER_NAME=%s and PASSWORD=%s'
        val=(username, password)
        cursor.execute(sql, val)
        dataset=cursor.fetchone()
        nv=None #Gia su khong tim thay nhan vien dung theo username + password
        if dataset!=None:
            ID, MANHANVIEN, TENNHANVIEN, USER_NAME, PASSWORD, IsDelete = dataset
            # Vao duoc day tuc la co nhan vien
            nv=NhanVien(ID, MANHANVIEN, TENNHANVIEN, USER_NAME, PASSWORD, IsDelete)

        cursor.close()
        return nv