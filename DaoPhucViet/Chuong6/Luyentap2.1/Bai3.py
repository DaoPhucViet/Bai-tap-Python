_tuple = ('ab', 'b', 'e', 'c', 'd', 'e', 'ab')
_new_tuple = ()
for item in _tuple:
    if item not in _new_tuple:   # đảm bảo không thêm lại
        _new_tuple += (item,)
print("Tuple mới:", _new_tuple)