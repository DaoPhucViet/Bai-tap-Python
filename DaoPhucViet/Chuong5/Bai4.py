# Nhập thông tin cá nhân
name = input("Nhập tên: ")
age = input("Nhập tuổi: ")
email = input("Nhập email: ")
skype = input("Nhập skype: ")
address = input("Nhập địa chỉ: ")
workplace = input("Nhập nơi làm việc: ")

# a) Ghi vào file setInfo.txt
with open("E:/vscode/Python/DaoPhucViet/Chuong5/setInfo.txt", "w", encoding="utf-8") as f:
    f.write(f"Tên: {name}\n")
    f.write(f"Tuổi: {age}\n")
    f.write(f"Email: {email}\n")
    f.write(f"Skype: {skype}\n")
    f.write(f"Địa chỉ: {address}\n")
    f.write(f"Nơi làm việc: {workplace}\n")

# b) Đọc lại file và hiển thị
with open("E:/vscode/Python/DaoPhucViet/Chuong5/setInfo.txt", "r", encoding="utf-8") as f:
    print("\nThông tin đã lưu:")
    print(f.read())
f.close