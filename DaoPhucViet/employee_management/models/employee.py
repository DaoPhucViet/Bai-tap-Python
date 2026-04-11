from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, emp_id, name, age, base_salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.base_salary = base_salary

        # mở rộng theo đề
        self.projects = []        # danh sách dự án
        self.performance = 0.0    # điểm hiệu suất (0-10)

    @abstractmethod
    def calculate_salary(self):
        pass

    # ========================
    # PROJECT
    # ========================
    def add_project(self, project):
        if len(self.projects) >= 5:
            raise Exception("Không thể tham gia quá 5 dự án")
        self.projects.append(project)

    def remove_project(self, project):
        if project in self.projects:
            self.projects.remove(project)

    # ========================
    # PERFORMANCE
    # ========================
    def update_performance(self, score):
        if score < 0 or score > 10:
            raise ValueError("Điểm phải từ 0-10")
        self.performance = score

    # ========================
    # DISPLAY
    # ========================
    def __str__(self):
        return (
            f"ID: {self.emp_id} | "
            f"Tên: {self.name} | "
            f"Tuổi: {self.age} | "
            f"Lương: {self.calculate_salary():,.0f} | "
            f"Hiệu suất: {self.performance}"
        )