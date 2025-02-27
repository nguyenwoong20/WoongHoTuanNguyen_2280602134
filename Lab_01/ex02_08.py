def chiahetcho5(sonhiphan):
    sothapphan = int(sonhiphan, 2)
    if sothapphan % 5 == 0:
        return True
    else:
        return False
chuoisonhiphan = input("Nhập vào một chuỗi số nhị phân (phân tách bởi dấu phẩy): ")
sonhiphanlist = chuoisonhiphan.split(',')
sochiahetcho5 = [so for so in sonhiphanlist if chiahetcho5(so)]
if len(sochiahetcho5) > 0:
    ketqua = ', '.join(sochiahetcho5)
    print("Các số nhị phân chi hết cho 5 là: ", ketqua)
else:
    print("Không có số nhị phân nào chi hết cho 5.")
def chiahetcho5(sonhiphan):
    sothapphan = int(sonhiphan, 2)
    if sothapphan % 5 == 0:
        return True
    else:
        return False