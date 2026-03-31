n = int(input("Nhap n: "))
if n > 20:
    print("Vui long nhap so nho hon 20")
else:
    for i in range (n,20):
        if i%5 ==0 or i%7==0:
            print(i)
