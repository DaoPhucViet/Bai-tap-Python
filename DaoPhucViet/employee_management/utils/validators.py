from exceptions.employee_exceptions import *

def validate_age(age):
    if age < 18 or age > 65:
        raise InvalidAgeError("Tuổi phải từ 18 đến 65")

def validate_salary(salary):
    if salary <= 0:
        raise InvalidSalaryError("Lương phải > 0")

def validate_performance(score):
    if score < 0 or score > 10:
        raise ValueError("Điểm hiệu suất phải từ 0-10")

def validate_email(email):
    if "@" not in email:
        raise ValueError("Email không hợp lệ")

def validate_menu_choice(choice, min_val=0, max_val=9):
    try:
        choice = int(choice)
    except:
        raise ValueError("Phải nhập số")

    if choice < min_val or choice > max_val:
        raise ValueError(f"Chọn từ {min_val} đến {max_val}")

    return choice

def validate_non_empty(value, field_name="Giá trị"):
    if not value.strip():
        raise ValueError(f"{field_name} không được để trống")