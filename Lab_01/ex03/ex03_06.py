def xoaphantu(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
key_to_delete = 'b'
result = xoaphantu(my_dict, key_to_delete)
if result:
    print("Xóa phần tử thành công.")
    print("Dictionary sau khi xóa phần tử:", my_dict)
else:
    print("Không thể xóa phần tử vì không tìm thấy key trong dictionary.")