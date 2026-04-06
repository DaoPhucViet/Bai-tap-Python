list = [1,2,3,4,5,6,7,8,9]
evenList = []
oddList = []
for i in range(0,len(list)):
    if list[i] % 2 == 0:
        evenList.append(list[i])
    else:
        oddList.append(list[i])
print(evenList)
print(oddList)