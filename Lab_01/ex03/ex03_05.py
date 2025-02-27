def desolanxuathien(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

input_string = input("Nhập vào một dãy số, cách nhau bởi dấu cách: ")
word_list = input_string.split()

solansolanxuathien = desolanxuathien(word_list)
print("Số lần xuất hiện của mỗi phần tử:", solansolanxuathien)