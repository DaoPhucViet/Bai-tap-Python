from .employee import Employee

class Intern(Employee):
    def __init__(self, emp_id, name, age, base_salary):
        super().__init__(emp_id, name, age, base_salary)

    def calculate_salary(self):
        return self.base_salary * 0.8

    def __str__(self):
        return "[Intern] " + super().__str__()