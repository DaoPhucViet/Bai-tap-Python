list =  ['abc', 'xyz', 'aba', '1221', 'ii', 'ii2', '5yhy5'] 
n=int(input("Nhap n: "))
ketqua = 0
for i in range(0,len(list)):
    if len(list[i]) >=n:
        ketqua +=1
print(ketqua)