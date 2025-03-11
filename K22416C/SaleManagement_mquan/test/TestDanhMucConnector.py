from SaleManagement.libs.danhmucconnector import DanhMucConnector

dmc = DanhMucConnector()
dmc.connect()
dsdm = dmc.LayToanBoDanhMuc()
print("Danh muc san pham ")
for dm in dsdm:
    print(dm)