class HocVien:
    def __init__(self,ten,ngaysinh,email,sdt,diachi,lop):
        self.ten = ten
        self.ngaysinh = ngaysinh
        self.email = email
        self.sdt = sdt
        self.diachi = diachi
        self.lop = lop
    
    def show_info(self):
        print("Họ tên: ",self.ten)
        print("Ngày sinh: ",self.ngaysinh)
        print("Email: ",self.email)
        print("Số điện thoại: ",self.sdt)
        print("Địa chỉ: ",self.diachi)
        print("Lớp: ",self.lop)
    
    def setInfo(self,diachi = "Hà Nội", lop = "IT12.x"):
        self.diachi = diachi
        self.lop = lop

class Main:
    hv1 = HocVien("Đào Phúc Việt","13/05/2005","Viet@gmail.com","0965323618","Hưng Yên","IT14.2")
    hv1.show_info()
    print("--------------------")
    hv1.setInfo()
    hv1.show_info()