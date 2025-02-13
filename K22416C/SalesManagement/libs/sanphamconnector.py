from K22416C.SalesManagement.libs.connector import MySQLConnector
from K22416C.SalesManagement.models.sanpham import SanPham


class SanPhamConnector(MySQLConnector):
    def LaySanPhamTheoMaDanhMuc(self, iddm):
        cursor = self.conn.cursor()
        sql="select * from DANHMUC where ID_DANHMUC=%s"
        val=(iddm,)
        cursor.execute(sql, val)
        dataset=cursor.fetchall()
        dssp=[]
        for item in dataset:
            dssp.append(SanPham(item[0], item[1], item[2], item[3], item[4], item[5]))
        cursor.close()
        return dssp

    def Lay_ChiTiet(self, ID):
        cursor=self.conn.cursor()
        sql='Select * from SANPHAM where ID=%s'
        val=(ID, )
        cursor.execute(sql, val)
        dataset=cursor.fetchone()
        sp=None
        if dataset!=None:
            ID, ma, ten, soluong, dongia, iddm = dataset
            # Vao duoc day tuc la co nhan vien
            sp=SanPham(id, ma, ten, soluong, dongia, iddm)
        cursor.close()
        return sp

    def Xoa_SanPham(self,ID):
        cursor=self.conn.cursor()
        sql='delete from SANPHAM where ID=%s'
        val=(ID, )
        cursor.execute(sql, val)
        self.conn.commit()
        # So dong du lieu thanh cong bi anh huong
        result=cursor.rowcount
        cursor.close()
        return result
