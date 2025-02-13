import traceback

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QListWidgetItem, QTableWidgetItem, QMessageBox

from K22416C.SalesManagement.UI.ProductMainWindow import Ui_MainWindow
from K22416C.SalesManagement.libs.danhmucconnector import DanhMucConnector
from K22416C.SalesManagement.libs.sanphamconnector import SanPhamConnector


class ProductMainWindowExt(Ui_MainWindow):
    def __init__(self):
        self.dmc=DanhMucConnector()
        self.dsdm=[]
        self.spc=SanPhamConnector()
        self.dssp=[]
        self.current_selected_danhmuc=None

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.truyvan_danhmucsanpham()
        self.hienthi_danhmucsanpham()
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()

    def truyvan_danhmucsanpham(self):
        self.dmc.connect()
        self.dsdm=self.dmc.LayToanBoDanhMuc()

    def hienthi_danhmucsanpham(self):
        #Xoá toàn bộ dữ liệu cũ trên giao diện
        self.listWidgetDanhMuc.clear()
        for dm in self.dsdm:
            item=QListWidgetItem()
            item.setData(Qt.ItemDataRole.UserRole, dm)
            item.setText(str(dm.ten))
            self.listWidgetDanhMuc.addItem(item)

    def setupSignalAndSlot(self):
        self.listWidgetDanhMuc.itemSelectionChanged.connect(self.tai_danhsach_sanpham)
        self.tableWidgetSanPham.itemSelectionChanged.connect(self.xem_chitiet_sanpham)
        self.pushButtonXoa.clicked.connect(self.Xuly_xoa())

    def tai_danhsach_sanpham(self):
        selected_index=self.listWidgetDanhMuc.currentRow()
        if selected_index < 0: #Chua chon gi
            return
        item=self.listWidgetDanhMuc.item(selected_index)
        dm=item.data(Qt.ItemDataRole.UserRole)
        self.spc.connect()
        self.dssp=self.spc.LaySanPhamTheoMaDanhMuc(dm.id)

        for p in self.dssp:
            print(p)

        self.hienthi_danhsach_sanpham_len_qtable()
    def hienthi_danhsach_sanpham_len_qtable(self):
        try:
            # Xoa du lieu cu tren QTableWidget
            self.tableWidgetSanPham.setRowCount(0)
            for p in self.dssp:
                # Lay vi tri cua dong cuoi cung +1 (la dong moi):
                row_index=self.tableWidgetSanPham.rowCount()
                # Thuc hien chen moi 1 dong vao cuoi bang:
                self.tableWidgetSanPham.insertRow(row_index)
                # Vi moi dong co 6 cot. Ta hien thi gia tri cho tung cot:
                cot_id=QTableWidgetItem(str(p.id))
                cot_ma=QTableWidgetItem(str(p.MASANPHAM))
                cot_ten=QTableWidgetItem(str(p.TENSANPHAM))
                cot_soluong=QTableWidgetItem(str(p.SOLUONG))
                cot_dongia=QTableWidgetItem(str(p.DONGIA))
                cot_iddm=QTableWidgetItem(str(p.ID_DANHMUC))

                self.tableWidgetSanPham.setItem(row_index, 0, cot_id)
                self.tableWidgetSanPham.setItem(row_index, 1, cot_ma)
                self.tableWidgetSanPham.setItem(row_index, 2, cot_ten)
                self.tableWidgetSanPham.setItem(row_index, 3, cot_soluong)
                self.tableWidgetSanPham.setItem(row_index, 4, cot_dongia)
                self.tableWidgetSanPham.setItem(row_index, 5, cot_iddm)

                if p.SOLUONG <=20:
                    cot_soluong.setBackground(Qt.GlobalColor.yellow)
                    cot_soluong.setForeground(Qt.GlobalColor.red)
        except:
            traceback.print_exc()

    def xem_chitiet_sanpham(self):
        selected_index=self.tableWidgetSanPham.currentRow()
        if selected_index==-1:
            return
        id=self.tableWidgetSanPham.item(selected_index,0).text()
        self.spc.connect()
        sp=self.spc.Lay_ChiTiet(id)

        if sp!=None:
            self.lineEditID.setText(str(sp.ID))
            self.lineEditMa.setText(str(sp.MASANPHAM))
            self.lineEditTen.setText(str(sp.TENSANPHAM))
            self.lineEditSoLuong.setText(str(sp.SOLUONG))
            self.lineEditDonGia.setText(str(sp.DONGIA))
            self.lineEditIDDM.setText(str(sp.ID_DANHMUC))

    def Xuly_xoa(self):
        msg=self.lineEditID.text()+"-"+self.lineEditTen.text()
        dlg=QMessageBox(self.MainWindow)
        dlg.setWindowTitle("Xac thuc xoa")
        dlg.setText("E, muon xoa san pham ["+msg +" ha?")
        dlg.setIcon(QMessageBox.Icon.Question)
        button=QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.No
        dlg.setStandardButtons(button)
        result=dlg.exec()
        if result==QMessageBox.StandardButton.No:
            return
        self.spc.connect()
        result=self.spc.Xoa_SanPham(self.lineEditID.text())
        if result>0:
            self.spc.connect()
            self.dssp=self.spc.LaySanPhamTheoMaDanhMuc(self.current_selected_danhmuc.ID)
            self.hienthi_danhsach_sanpham_len_qtable()