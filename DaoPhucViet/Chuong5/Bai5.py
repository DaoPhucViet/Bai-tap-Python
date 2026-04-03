from collections import Counter

with open("E:/vscode/Python/DaoPhucViet/Chuong5/demo_file2.txt", "w", encoding="utf-8") as f:
    f.write("Dem so luong tu xuat hien abc abc abc 12 12 it it eaut")

# Đọc file
with open("E:/vscode/Python/DaoPhucViet/Chuong5/demo_file2.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Tách từ và đếm số lần xuất hiện
words = content.split()
count = Counter(words)

# In kết quả
print(dict(count))