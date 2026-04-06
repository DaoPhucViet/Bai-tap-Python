_list = ['abc', 'xyz', 'abc', '12', 'ii', '12', '5a']
newlist=[]
for x in _list:
    if _list.count(x) == 1:
        newlist.append(x)
print(newlist)
    
