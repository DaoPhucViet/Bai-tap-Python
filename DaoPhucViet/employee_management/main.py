from models.manager import Manager
from models.developer import Developer
from models.intern import Intern
from services.company import Company
from utils.validators import *

company = Company()

# ================= MENU CHÍNH =================
def show_main_menu():
    print("\n" + "="*60)
    print("      HỆ THỐNG QUẢN LÝ NHÂN VIÊN CÔNG TY ABC")
    print("="*60)
    print("1. Thêm nhân viên")
    print("2. Hiển thị danh sách nhân viên")
    print("3. Tìm kiếm nhân viên")
    print("4. Quản lý lương")
    print("5. Quản lý dự án")
    print("6. Đánh giá hiệu suất")
    print("7. Quản lý nhân sự")
    print("8. Báo cáo")
    print("9. Thoát")
    print("="*60)

# ================= MENU CON =================
def menu_add():
    print("\n--- THÊM NHÂN VIÊN ---")
    print("a. Manager")
    print("b. Developer")
    print("c. Intern")

def menu_show():
    print("\n--- DANH SÁCH ---")
    print("a. Tất cả")
    print("b. Theo loại")
    print("c. Theo hiệu suất")

def menu_find():
    print("\n--- TÌM KIẾM ---")
    print("a. Theo ID")
    print("b. Theo tên")
    print("c. Theo ngôn ngữ")

def menu_salary():
    print("\n--- LƯƠNG ---")
    print("a. Lương từng nhân viên")
    print("b. Tổng lương")
    print("c. Top 3")

def menu_hr():
    print("\n--- NHÂN SỰ ---")
    print("a. Xoá")
    print("b. Tăng lương")
    print("c. Thăng chức")

# ================= CHỨC NĂNG =================

def input_employee(option):
    try:
        emp_id = input("ID: ")
        name = input("Tên: ")
        age = int(input("Tuổi: "))
        salary = float(input("Lương cơ bản: "))

        validate_age(age)
        validate_salary(salary)

        if option == "a":
            emp = Manager(emp_id, name, age, salary)
        elif option == "b":
            lang = input("Ngôn ngữ: ")
            emp = Developer(emp_id, name, age, salary, lang)
        else:
            emp = Intern(emp_id, name, age, salary)

        company.add_employee(emp)
        print("✔ Thành công")

    except Exception as e:
        print("❌", e)

def show_all():
    for e in company.get_all():
        print(e)

def find_by_id():
    try:
        emp_id = input("ID: ")
        print(company.find_by_id(emp_id))
    except Exception as e:
        print(e)

def salary_action(option):
    if option == "a":
        for e in company.get_all():
            print(e, "=>", e.calculate_salary())
    elif option == "b":
        print("Tổng lương:", company.total_salary())
    elif option == "c":
        for e in company.top_salary():
            print(e)

def delete_emp():
    try:
        emp_id = input("ID: ")
        company.remove_employee(emp_id)
        print("✔ Đã xoá")
    except Exception as e:
        print(e)

# ================= MAIN =================
def main():
    while True:
        show_main_menu()
        choice = input("Chọn chức năng (1-9): ")

        # ===== 1 =====
        if choice == "1":
            menu_add()
            sub = input("Chọn (a/b/c): ")
            input_employee(sub)

        # ===== 2 =====
        elif choice == "2":
            menu_show()
            sub = input("Chọn (a/b/c): ")
            if sub == "a":
                show_all()

        # ===== 3 =====
        elif choice == "3":
            menu_find()
            sub = input("Chọn (a/b/c): ")
            if sub == "a":
                find_by_id()

        # ===== 4 =====
        elif choice == "4":
            menu_salary()
            sub = input("Chọn (a/b/c): ")
            salary_action(sub)

        # ===== 5 =====
        elif choice == "5":
            print("⚠ Chưa làm project")

        # ===== 6 =====
        elif choice == "6":
            print("⚠ Chưa làm performance")

        # ===== 7 =====
        elif choice == "7":
            menu_hr()
            sub = input("Chọn (a/b/c): ")
            if sub == "a":
                delete_emp()

        # ===== 8 =====
        elif choice == "8":
            print("⚠ Chưa làm report")

        # ===== 9 =====
        elif choice == "9":
            print("Thoát...")
            break

        else:
            print("❌ Sai lựa chọn")

if __name__ == "__main__":
    main()