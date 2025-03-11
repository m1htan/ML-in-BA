from SaleManagement.libs.sanphamconnector import SanPhamConnector

spc = SanPhamConnector()
spc.connect()
dssp = spc.LaySanPhamTheoDanhMuc(1)
print("Danh sach co ma danh muc = 1")
for p in dssp:
    print(p)

id = 2
spc.connect()
sp = spc.Lay_chitiet(id)
if sp!= None:
    print("*"*20)
    print(sp)

id_remove = 13
spc.connect()
result = spc.xoa_sanpham(id_remove)
if result>0:
    print("Xoa san pham co ma =", id_remove,"thanh cong")
else:
    print("That bai")
