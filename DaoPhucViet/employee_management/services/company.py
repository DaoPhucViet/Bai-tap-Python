from exceptions.employee_exceptions import *

class Company:
    def __init__(self):
        self.employees = []

    # =========================
    # 1. THÊM NHÂN VIÊN
    # =========================
    def add_employee(self, emp):
        if any(e.emp_id == emp.emp_id for e in self.employees):
            raise DuplicateEmployeeError()
        self.employees.append(emp)

    # =========================
    # 2. HIỂN THỊ
    # =========================
    def get_all(self):
        if not self.employees:
            raise IndexError("Chưa có dữ liệu")
        return self.employees

    def filter_by_type(self, emp_type):
        return [e for e in self.employees if e.__class__.__name__ == emp_type]

    def sort_by_performance(self):
        return sorted(self.employees, key=lambda e: e.performance, reverse=True)

    # =========================
    # 3. TÌM KIẾM
    # =========================
    def find_by_id(self, emp_id):
        for e in self.employees:
            if e.emp_id == emp_id:
                return e
        raise EmployeeNotFoundError(emp_id)

    def find_by_name(self, name):
        return [e for e in self.employees if name.lower() in e.name.lower()]

    def find_by_language(self, language):
        return [
            e for e in self.employees
            if hasattr(e, "language") and e.language.lower() == language.lower()
        ]

    # =========================
    # 4. QUẢN LÝ LƯƠNG
    # =========================
    def calculate_salary_employee(self, emp_id):
        emp = self.find_by_id(emp_id)
        return emp.calculate_salary()

    def total_salary(self):
        return sum(e.calculate_salary() for e in self.employees)

    def top_3_salary(self):
        return sorted(self.employees, key=lambda e: e.calculate_salary(), reverse=True)[:3]

    # =========================
    # 5. QUẢN LÝ DỰ ÁN
    # =========================
    def assign_project(self, emp_id, project):
        emp = self.find_by_id(emp_id)

        if len(emp.projects) >= 5:
            raise ProjectAllocationError("Nhân viên đã có 5 dự án")

        emp.add_project(project)

    def remove_project(self, emp_id, project):
        emp = self.find_by_id(emp_id)
        emp.remove_project(project)

    def get_projects_of_employee(self, emp_id):
        emp = self.find_by_id(emp_id)
        return emp.projects

    # =========================
    # 6. HIỆU SUẤT
    # =========================
    def update_performance(self, emp_id, score):
        emp = self.find_by_id(emp_id)
        if score < 0 or score > 10:
            raise ValueError("Điểm phải từ 0-10")
        emp.update_performance(score)

    def excellent_employees(self):
        return [e for e in self.employees if e.performance > 8]

    def low_performance_employees(self):
        return [e for e in self.employees if e.performance < 5]

    # =========================
    # 7. QUẢN LÝ NHÂN SỰ
    # =========================
    def remove_employee(self, emp_id):
        emp = self.find_by_id(emp_id)
        self.employees.remove(emp)

    def increase_salary(self, emp_id, amount):
        emp = self.find_by_id(emp_id)
        emp.base_salary += amount

    def promote(self, emp_id):
        emp = self.find_by_id(emp_id)

        from models.intern import Intern
        from models.developer import Developer
        from models.manager import Manager

        if isinstance(emp, Intern):
            new_emp = Developer(emp.emp_id, emp.name, emp.age, emp.base_salary, "Python")
        elif isinstance(emp, Developer):
            new_emp = Manager(emp.emp_id, emp.name, emp.age, emp.base_salary)
        else:
            return "Không thể thăng chức"

        # giữ lại dữ liệu cũ
        new_emp.projects = emp.projects
        new_emp.performance = emp.performance

        self.employees.remove(emp)
        self.employees.append(new_emp)

    # =========================
    # 8. BÁO CÁO
    # =========================
    def count_by_type(self):
        result = {}
        for e in self.employees:
            t = e.__class__.__name__
            result[t] = result.get(t, 0) + 1
        return result

    def total_salary_by_type(self):
        result = {}
        for e in self.employees:
            t = e.__class__.__name__
            result[t] = result.get(t, 0) + e.calculate_salary()
        return result

    def avg_projects_per_employee(self):
        if not self.employees:
            return 0
        total = sum(len(e.projects) for e in self.employees)
        return total / len(self.employees)