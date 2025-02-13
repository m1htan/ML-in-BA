class DanhMuc:
    def __init__(self, ID, MADANHMUC, TENDANHMUC):
        self.ID=ID
        self.MADANHMUC=MADANHMUC
        self.TENDANHMUC=TENDANHMUC

    def __str__(self):
        return f"{self.id}\t{self.MADANHMUC}\t{self.TENDANHMUC}"
