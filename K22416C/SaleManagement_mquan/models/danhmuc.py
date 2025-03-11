class DanhMuc:
    def __init__(self, id, madanhmuc, tendanhmuc):
        self.id = id
        self.madanhmuc = madanhmuc
        self.tendanhmuc = tendanhmuc
    def __str__(self):
        return f"{self.id}\t{self.madanhmuc}\t{self.tendanhmuc}"
