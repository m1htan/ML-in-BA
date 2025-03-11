from K22416C.SaleManagement_mquan.libs.connector import MySqlConnector
from K22416C.SaleManagement_mquan.models.sanpham import SanPham


class SanPhamConnector(MySqlConnector):
    def LaySanPhamTheoDanhMuc(self,iddm):
        cursor = self.conn.cursor()
        sql = "select * from sanpham where iddanhmuc=%s "
        val= (iddm,)
        cursor.execute(sql, val)
        dataset = cursor.fetchall()
        dssp = []
        for item in dataset:
            dssp.append(SanPham(item[0], item[1], item[2], item[3], item[4], item[5]))
        cursor.close()
        return dssp

    def Lay_chitiet(self, id):
        cursor = self.conn.cursor()
        sql = "select * from sanpham where id=%s"
        val = (id,)
        cursor.execute(sql, val)
        dataset = cursor.fetchone()
        sp = None
        if dataset != None:
            id, ma, ten, sl, dg, iddm = dataset
            sp = SanPham(id, ma, ten, sl, dg, iddm)
        cursor.close()
        return sp
    def xoa_sanpham(self,id):
        cursor = self.conn.cursor()
        sql = "delete from sanpham where id=%s"
        val = (id,)
        cursor.execute(sql, val)
        self.conn.commit()
        result = cursor.rowcount
        cursor.close()
        return result