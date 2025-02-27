def daonguoclist(lst):
    return lst[::-1]
inputlist = input("Nhập vào một dãy số, cách nhau bởi dấu phẩy: ")
number = list(map(int, inputlist.split(',')))
listdao = daonguoclist(number)
print("Dãy số đảo ngược:", listdao)