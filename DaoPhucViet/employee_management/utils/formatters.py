def print_header(title):
    print("\n" + "="*50)
    print(f"{title.center(50)}")
    print("="*50)

def print_employee(emp):
    print(emp)

def print_employee_list(emp_list):
    if not emp_list:
        print("⚠ Không có dữ liệu")
        return

    print_header("DANH SÁCH NHÂN VIÊN")
    for e in emp_list:
        print(e)

def print_top_3(emp_list):
    print_header("TOP 3 LƯƠNG CAO NHẤT")
    for i, e in enumerate(emp_list, 1):
        print(f"{i}. {e}")

def print_projects(projects):
    if not projects:
        print("Chưa có dự án")
        return

    print("Danh sách dự án:")
    for p in projects:
        print(f"- {p}")

def print_statistics(data, title="THỐNG KÊ"):
    print_header(title)
    for key, value in data.items():
        print(f"{key}: {value}")

def print_line():
    print("-"*50)