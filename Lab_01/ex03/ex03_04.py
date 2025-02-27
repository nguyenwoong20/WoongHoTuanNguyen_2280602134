def truycapphantu(tuple_data):
    first_element = tuple_data[0]
    last_element = tuple_data[-1]
    return first_element, last_element

input_str = eval(input("Nhập vào một tuple, ví dụ (1, 2, 3): "))
first, last = truycapphantu(input_str)

print("Phần tử đầu tiên và cuối cùng của tuple là:", first, last)