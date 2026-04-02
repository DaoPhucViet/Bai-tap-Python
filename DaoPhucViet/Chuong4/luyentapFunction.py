import math

# 1. Tính tổng 2 số
def tong_2_so(a, b):
    return a + b

# 2. Tính tổng các số truyền vào (dùng list)
def tong_danh_sach(ds):
    return sum(ds)

# 3. Kiểm tra số nguyên tố
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# 4. Tìm số nguyên tố trong đoạn [a, b]
def tim_snt_trong_doan(a, b):
    kq = []
    for i in range(a, b + 1):
        if la_so_nguyen_to(i):
            kq.append(i)
    return kq

# 5. Kiểm tra số hoàn hảo
def la_so_hoan_hao(n):
    if n <= 0:
        return False
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong == n

# 6. Tìm số hoàn hảo trong đoạn [a, b]
def tim_shh_trong_doan(a, b):
    kq = []
    for i in range(a, b + 1):
        if la_so_hoan_hao(i):
            kq.append(i)
    return kq

# ===== MENU =====
def menu():
    while True:
        print("\n===== MENU =====")
        print("1. Tính tổng 2 số")
        print("2. Tính tổng danh sách số")
        print("3. Kiểm tra số nguyên tố")
        print("4. Tìm số nguyên tố trong [a,b]")
        print("5. Kiểm tra số hoàn hảo")
        print("6. Tìm số hoàn hảo trong [a,b]")
        print("0. Thoát")

        chon = int(input("Chọn: "))

        if chon == 1:
            a = int(input("Nhập a: "))
            b = int(input("Nhập b: "))
            print("Tổng =", tong_2_so(a, b))

        elif chon == 2:
            ds = list(map(int, input("Nhập các số cách nhau bằng dấu cách: ").split()))
            print("Tổng =", tong_danh_sach(ds))

        elif chon == 3:
            n = int(input("Nhập n: "))
            if la_so_nguyen_to(n):
                print("Là số nguyên tố")
            else:
                print("Không phải số nguyên tố")

        elif chon == 4:
            a = int(input("Nhập a: "))
            b = int(input("Nhập b: "))
            print("Các số nguyên tố:", tim_snt_trong_doan(a, b))

        elif chon == 5:
            n = int(input("Nhập n: "))
            if la_so_hoan_hao(n):
                print("Là số hoàn hảo")
            else:
                print("Không phải số hoàn hảo")

        elif chon == 6:
            a = int(input("Nhập a: "))
            b = int(input("Nhập b: "))
            print("Các số hoàn hảo:", tim_shh_trong_doan(a, b))

        elif chon == 0:
            print("Thoát chương trình.")
            break

        else:
            print("Chọn sai, nhập lại!")

# Chạy chương trình
menu()