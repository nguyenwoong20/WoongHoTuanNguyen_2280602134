#nhập các dòng từ người dùng
print("Nhập các dòng văn bản (nhập 'd' đển kêt thúc):")
lines = []
while True:
    line = input()
    if line == 'd':
        break
    lines.append(line)
#chuyển các dòng thành chữ in hoa và in ra màn hình
print("Các dòng đã nhập sau khi Chuyển thành chữ in hoa:")
for line in lines:
    print(line.upper())