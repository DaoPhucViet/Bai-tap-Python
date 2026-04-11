class Payroll:

    @staticmethod
    def calculate_employee(emp):
        return emp.calculate_salary()

    @staticmethod
    def total_company(company):
        return company.total_salary()

    @staticmethod
    def top_3(company):
        return company.top_3_salary()