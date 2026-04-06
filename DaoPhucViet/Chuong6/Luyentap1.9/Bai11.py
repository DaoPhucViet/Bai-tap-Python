n = int(input("Nhap n: "))
_list = ["hai","ba","bon"]
_hon_n =[]
for i in range (0,len(_list)):
    if len(_list[i]) > n:
        _hon_n.append(_list[i])
print("Cac tu co do dai lon hon n la: ",_hon_n)