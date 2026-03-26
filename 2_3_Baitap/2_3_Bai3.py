a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))

# a) Tổng và trung bình cộng
tong = a + b + c
tbc = tong / 3
print("Tổng:", tong)
print("Trung bình cộng:", tbc)

# b) Hiệu (ví dụ: a - b, b - c, a - c)
print("Hiệu a - b:", a - b)
print("Hiệu b - c:", b - c)
print("Hiệu a - c:", a - c)

# c) Chia (ví dụ a chia b)
if b != 0:
    print("a // b =", a // b)   # chia lấy phần nguyên
    print("a % b =", a % b)    # chia lấy dư
    print("a / b =", a / b)    # chia chính xác
else:
    print("Không thể chia cho 0")