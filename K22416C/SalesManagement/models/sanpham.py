class SanPham:
    def __init__(self, ID, MASANPHAM, TENSANPHAM, SOLUONG, DONGIA, ID_DANHMUC):
        self.ID=ID
        self.MASANPHAM=MASANPHAM
        self.TENSANPHAM=TENSANPHAM
        self.SOLUONG=SOLUONG
        self.DONGIA=DONGIA
        self.ID_DANHMUC=ID_DANHMUC

    def __str__(self):
        msg=f"{self.ID}\t{self.MASANPHAM}\t{self.TENSANPHAM}\t{self.SOLUONG}\t{self.DONGIA}\t{self.ID_DANHMUC}"
        return msg