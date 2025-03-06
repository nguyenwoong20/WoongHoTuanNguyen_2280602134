from SinhVien import SinhVien

class QuanLySinhVien:
    def __init__(self):
        self.list_sv = []
    
    def generateID(self):
        return max((sv._mssv for sv in self.list_sv), default=0) + 1
    
    def SoLuongSinhVien(self):  
        return len(self.list_sv)
    
    def nhapSinhVien(self):
        svID = self.generateID()
        ho_ten = input("Nhap ho ten: ")
        gioitinh = input("Nhap gioi tinh: ")
        cn = input("Nhap chuyen nganh: ")
        diem = float(input("Nhap diem: "))
        sv = SinhVien(svID, ho_ten, gioitinh, cn, diem)
        self.XepLoaiHocLuc(sv)
        self.list_sv.append(sv)
        print("\nThem sinh vien thanh cong!!!")
        
    def UpdateSinhVien(self, mssv):
        sv = self.findByID(mssv)
        if sv:
            sv._ho_ten = input("Nhap ho ten moi: ")
            sv._gioitinh = input("Nhap gioi tinh moi: ")
            sv._cn = input("Nhap chuyen nganh moi: ")
            sv._diem = float(input("Nhap diem moi: "))
            self.XepLoaiHocLuc(sv)
            print("\nCap nhat thong tin thanh cong!")
        else:
            print("\nSinh vien khong ton tai!")
    
    def sortbyDiem(self):
        self.list_sv.sort(key=lambda x: x._diem, reverse=True)
    
    def sortbyName(self):
        self.list_sv.sort(key=lambda x: x._ho_ten.lower())
    
    def findByID(self, mssv):
        return next((sv for sv in self.list_sv if sv._mssv == mssv), None)
    
    def findbyName(self, name):
        return [sv for sv in self.list_sv if name.lower() in sv._ho_ten.lower()]
    
    def deleteByID(self, mssv):
        for i, sv in enumerate(self.list_sv):
            if sv._mssv == mssv:
                del self.list_sv[i]
                print(f"\nSinh Vien có MSSV = {mssv} da bi xoa")
                return True
        print(f"\nSinh Vien có MSSV = {mssv} khong ton tai")
        return False
    
    def XepLoaiHocLuc(self, sv):
        if sv._diem >= 8:
            sv._hocluc = "Gioi"
        elif sv._diem >= 6.5:
            sv._hocluc = "Kha"
        elif sv._diem >= 5:
            sv._hocluc = "Trung Binh"
        else:
            sv._hocluc = "Yeu"
    
    def showSinhVien(self, listSV=None):
        if listSV is None:
            listSV = self.list_sv
        if not listSV:
            print("Danh sach sinh vien rong!\n")
            return
        print("{:<8} {:<18} {:<8} {:<15} {:<8} {:<8}".format("MSSV", "Ho Ten", "Gioi Tinh", "Chuyen Nganh", "Diem", "Hoc Luc"))
        for sv in listSV:
            print("{:<8} {:<18} {:<8} {:<15} {:<8} {:<8}".format(sv._mssv, sv._ho_ten, sv._gioitinh, sv._cn, sv._diem, sv._hocluc))
    
    def getlistSV(self):
        return self.list_sv