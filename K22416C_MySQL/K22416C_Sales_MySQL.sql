/* Câu 1: Viết câu lệnh SQL trả về toàn bộ sản phẩm */
Select * from SANPHAM

/* Câu 2: Viết lệnh SQL sắp xếp sản phầm theo đơn giá giảm dần */
select *
from SANPHAM
order by DONGIA desc

/* Câu 3: Xuất sản phầm có cột thành tiền và sắp xếp tăng dần */
Select *, SOLUONG*DONGIA as THANHTIEN
from SANPHAM
order by THANHTIEN asc

/* Câu 4: Viết câu lệnh SQL lấy toàn bộ danh mục */
Select * from DANHMUC

/* Câu 5: Lọc ra các sản phẩm thuộc về một danh mục bất kỳ */
Select *
from SANPHAM
Where ID_DANHMUC=1

/* Câu 6: Lọc ra các hoá đơn của một khách hàng bất kỳ */
Select *
from HOADON
Where ID_KHACHHANG=1

/* Câu 7: Xuất khách hàng có số hoá đơn nhiều nhất */
select ID_khachhang, count(*) as SoHoaDon
from hoadon
group by ID_khachhang
order by SoHoaDon desc
limit 1;

/* Câu 8: Xuất khách hàng có trị giá hoá đơn cao nhất */
select h.ID_khachhang, sum(ct.soluong * ct.dongia) as TongTriSoHoaDon
from hoadon h
join chitiethoadon ct on h.ID = ct.ID_hoadon
group by h.ID_khachhang
order by TongTriSoHoaDon desc
limit 1;





