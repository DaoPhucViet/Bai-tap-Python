from .employee import Employee

class Manager(Employee):
    def __init__(self, emp_id, name, age, base_salary):
        super().__init__(emp_id, name, age, base_salary)

    def calculate_salary(self):
        # Manager lương cao nhất
        return self.base_salary * 2

    def __str__(self):
        return "[Manager] " + super().__str__()