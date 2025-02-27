def tinhtongsochan(lst):
    tong = 0
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong
input_list = input("Nhập vào một dãy số, cách nhau bởi dấu phẩy: ")
number = list(map(int, input_list.split(',')))

tongchan = tinhtongsochan(number)
print("Tổng các số chẵn trong dãy là:", tongchan)
