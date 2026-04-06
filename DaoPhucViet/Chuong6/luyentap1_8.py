# Bảng mã
code_dict = {'a': '!', 'b': '@', 'c': '#', 'd': '$'}
# Tạo bảng giải mã (đảo key-value)
decode_dict = {v: k for k, v in code_dict.items()}
# Hàm mã hóa
def encode(text):
    result = ""
    for ch in text:
        if ch in code_dict:
            result += code_dict[ch]
        else:
            result += ch   # giữ nguyên nếu không có trong bảng mã
    return result
# Hàm giải mã
def decode(text):
    result = ""
    for ch in text:
        if ch in decode_dict:
            result += decode_dict[ch]
        else:
            result += ch
    return result
# Test
s = "abcd xyz"
encoded = encode(s)
decoded = decode(encoded)
print("Chuỗi gốc:", s)
print("Mã hóa:", encoded)
print("Giải mã:", decoded)