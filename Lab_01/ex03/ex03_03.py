def tao_tuple_tu_list(lst):
    return tuple(lst)

inputlist = input("Nhập vào một dãy số, cách nhau bởi dấu phẩy: ")
number = list(map(int, inputlist.split(',')))
mytuple = tao_tuple_tu_list(number)
print("Tuple:", number)
print("Tuple từ List:", mytuple)
 