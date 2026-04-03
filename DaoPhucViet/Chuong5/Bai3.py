with open("DaoPhucViet/Chuong5/demo_file1.txt", "w", encoding="utf-8") as f:
    f.write("Thuc\nhanh\nvoi\nfile\nIO\n")
# a) In ra nội dung file trên một dòng
with open("DaoPhucViet/Chuong5/demo_file1.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content.replace("\n", " "))
# b) In ra nội dung file theo từng dòng
with open("DaoPhucViet/Chuong5/demo_file1.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
f.close