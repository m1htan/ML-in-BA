class SanPham:
    def __init__(self, id, masanpham, tensanpham, soluong, dongia, iddanhmuc):
        self.id = id
        self.masanpham = masanpham
        self.tensanpham = tensanpham
        self.soluong = soluong
        self.dongia = dongia
        self.iddanhmuc = iddanhmuc

    def __str__(self):
        msg = f"{self.id}\t{self.masanpham}\t" \
              f"{self.tensanpham}\t{self.soluong}\t" \
              f"{self.dongia}\t{self.iddanhmuc}"
        return msg
