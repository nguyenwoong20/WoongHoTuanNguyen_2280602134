from QuanLySinhVien import QuanLySinhVien

QLSV = QuanLySinhVien()
QLSV = QuanLySinhVien()
while True:
        print("\nCHUONG TRINH QUAN LY SINH VIEN")
        print("==========================================================")
        print("*** 1. Nhap sinh vien.                                 ***")
        print("*** 2. Cap nhat sinh vien boi MSSV.                    ***")
        print("*** 3. Xoa sinh vien boi MSSV.                         ***")
        print("*** 4. Tim kiem sinh vien theo ten.                    ***")
        print("*** 5. Sap xep sinh vien theo diem trung binh.         ***")
        print("*** 6. Sap xep sinh vien theo chuyen nganh.            ***")    
        print("*** 7. Hien thi danh sach sinh vien.                   ***")
        print("*** 0. Thoat                                           ***")
    
        key = input("Nhap lua chon cua ban: ")
        if key == "1":
            QLSV.nhapSinhVien()
        elif key == "2":
            mssv = int(input("Nhap MSSV can cap nhat: "))
            QLSV.UpdateSinhVien(mssv)
        elif key == "3":
            mssv = int(input("Nhap MSSV can xoa: "))
            QLSV.deleteByID(mssv)
        elif key == "4":
            name = input("Nhap ten de tim kiem: ")
            QLSV.showSinhVien(QLSV.findbyName(name))
        elif key == "5":
            QLSV.sortbyDiem()
            QLSV.showSinhVien()
        elif key == "6":
            QLSV.sortbyName()
            QLSV.showSinhVien()
        elif key == "7":
            QLSV.showSinhVien()
        elif key == "0":
            print("Cam on ban da su dung chuong trinh!!!")
            break
        else:
            print("Lua chon khong hop le! Vui long nhap lai.")