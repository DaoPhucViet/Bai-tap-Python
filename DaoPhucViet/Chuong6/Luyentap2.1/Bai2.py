_tuple = ('ab', 'b', 'e', 'c', 'd', 'e', 'ab')
_new_tuple = ()
for item in _tuple:
    if _tuple.count(item) == 1:
        _new_tuple += (item,)
print("Tuple mới:", _new_tuple)