from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QListWidgetItem, QTableWidgetItem, QMessageBox
from K22416C.SaleManagement_mquan.libs.danhmucconnector import DanhMucConnector
from K22416C.SaleManagement_mquan.libs.sanphamconnector import SanPhamConnector
from K22416C.SaleManagement_mquan.ui.ProductMainWindow import Ui_MainWindow


class ProductMainWindowExt(Ui_MainWindow):
    def __init__(self):
        self.dmc = DanhMucConnector()
        self.dsdm = []
        self.spc = SanPhamConnector()
        self.dssp = []
        self.current_selected_danhmuc = None

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.truyvan_danhmucsanpham()
        self.hienthi_danhmucsanpham()
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()

    def truyvan_danhmucsanpham(self):
        self.dmc.connect()
        self.dsdm = self.dmc.LayToanBoDanhMuc()

    def hienthi_danhmucsanpham(self):
        self.listWidgetDanhMuc.clear()
        for dm in self.dsdm:
            item = QListWidgetItem()
            item.setData(Qt.ItemDataRole.UserRole, dm)
            item.setText(dm.tendanhmuc)
            self.listWidgetDanhMuc.addItem(item)

    def setupSignalAndSlot(self):
        self.listWidgetDanhMuc.itemSelectionChanged.connect(self.tai_danhsach_sanpham)
        self.tableWidgetSanPham.itemSelectionChanged.connect(self.xem_chitiet_sanpham)
        self.pushButtonXoa.clicked.connect(self.xuly_xoa)

    def tai_danhsach_sanpham(self):
        select_index = self.listWidgetDanhMuc.currentRow()
        if select_index < 0:
            return
        item=self.listWidgetDanhMuc.item(select_index)
        dm = item.data(Qt.ItemDataRole.UserRole)
        self.spc.connect()
        self.dssp = self.spc.LaySanPhamTheoDanhMuc(dm.id)
        for p in self.dssp:
            print(p)
        self.hienthi_danhsach_sanpham_len_qtable()
        self.current_selected_danhmuc = dm

    def hienthi_danhsach_sanpham_len_qtable(self):
        self.tableWidgetSanPham.setRowCount(0)
        for p in self.dssp:
            row_index = self.tableWidgetSanPham.rowCount()
            self.tableWidgetSanPham.insertRow(row_index)
            cot_id = QTableWidgetItem(str(p.id))
            cot_ma = QTableWidgetItem(p.masanpham)
            cot_ten = QTableWidgetItem(p.tensanpham)
            cot_sl = QTableWidgetItem(str(p.soluong))
            cot_gia = QTableWidgetItem(str(p.dongia))
            cot_iddm = QTableWidgetItem(str(p.iddanhmuc))
            self.tableWidgetSanPham.setItem(row_index, 0, cot_id)
            self.tableWidgetSanPham.setItem(row_index, 1, cot_ma)
            self.tableWidgetSanPham.setItem(row_index, 2, cot_ten)
            self.tableWidgetSanPham.setItem(row_index, 3, cot_sl)
            self.tableWidgetSanPham.setItem(row_index, 4, cot_gia)
            self.tableWidgetSanPham.setItem(row_index, 5, cot_iddm)
            if p.soluong <= 20:
                cot_sl.setBackground(Qt.GlobalColor.yellow)
                cot_sl.setForeground(Qt.GlobalColor.red)

    def xem_chitiet_sanpham(self):
        select_index = self.tableWidgetSanPham.currentRow()
        if select_index == -1:
            return
        id=self.tableWidgetSanPham.item(select_index,0).text()
        self.spc.connect()
        sp = self.spc.Lay_chitiet(id)
        if sp !=None :
            self.lineEditId.setText(str(sp.id))
            self.lineEditMa.setText(sp.masanpham)
            self.lineEditTen.setText(sp.tensanpham)
            self.lineEditSoLuong.setText(str(sp.soluong))
            self.lineEditDonGia.setText(str(sp.dongia))
            self.lineEditIdDM.setText(str(sp.iddanhmuc))

    def xuly_xoa(self):
        msg = self.lineEditId.text() + " - " + self.lineEditTen.text()
        dlg = QMessageBox(self.MainWindow)
        dlg.setWindowTitle("Xác thực lựa chọn")
        dlg.setText(f"Xóa [{msg}]?")
        dlg.setIcon(QMessageBox.Icon.Question)
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        dlg.setStandardButtons(buttons)
        result = dlg.exec()

        if result == QMessageBox.StandardButton.No:
            return

        self.spc.connect()
        result = self.spc.xoa_sanpham(self.lineEditId.text())
        if result > 0:
            self.tai_danhsach_sanpham()
            self.dssp = self.spc.LaySanPhamTheoMaDanhMuc(self.current_selected_danhmuc.id)
            self.hienthi_danhsach_sanpham_len_qtable()
