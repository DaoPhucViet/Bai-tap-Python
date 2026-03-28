import time

# Lấy năm hiện tại
x = time.localtime()
year = x[0]

# Nhập năm sinh
namsinh = int(input("Nhập năm sinh: "))

# Tính tuổi
tuoi = year - namsinh

# In kết quả
print(f"Năm sinh {namsinh}, vậy bạn {tuoi} tuổi.")