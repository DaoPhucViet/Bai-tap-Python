text = input("Nhập đoạn văn bản: ")

# Ghi vào file
with open("E:/vscode/Python/DaoPhucViet/Chuong5/output.txt", "w", encoding="utf-8") as f:
    f.write(text)

# Đọc lại và hiển thị
with open("E:/vscode/Python/DaoPhucViet/Chuong5/output.txt", "r", encoding="utf-8") as f:
    print("Nội dung file:")
    print(f.read())
f.close