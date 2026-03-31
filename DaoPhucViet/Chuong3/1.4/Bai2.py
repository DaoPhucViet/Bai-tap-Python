n = int(input("Nhap so nguyen n: "))
if n > 10:
    print("So nhap vao phai be hon 10")
else:
    for i in range(1,n):
        if i % 2 == 0:
            print(i)