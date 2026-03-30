# Nhập số nguyên dương
n = int(input("Nhập số nguyên dương n: "))

if n % 2 == 0 and n % 3 == 0:
    print("Số chia hết cho cả 2 và 3")
elif n % 2 == 0:
    print("Số chia hết cho 2")
elif n % 3 == 0:
    print("Số chia hết cho 3")
else:
    print("Số không chia hết cho 2 và 3")