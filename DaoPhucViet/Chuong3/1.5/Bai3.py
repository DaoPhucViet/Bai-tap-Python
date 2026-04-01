import math
n = int(input("Nhập một số: "))
is_prime = True

if n <= 1:
    is_prime = False
else:
    i = 2
    # Sử dụng vòng lặp while để kiểm tra
    while i <= math.sqrt(n):
        if n % i == 0:
            is_prime = False
            break
        i += 1

if is_prime:
    print(n, "là số nguyên tố")
else:
    print(n, "không phải là số nguyên tố")