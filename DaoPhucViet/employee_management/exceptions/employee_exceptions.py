class EmployeeException(Exception):
    """Base exception cho hệ thống nhân viên"""
    pass


# =========================
# KHÔNG TÌM THẤY NHÂN VIÊN
# =========================
class EmployeeNotFoundError(EmployeeException):
    def __init__(self, emp_id):
        self.emp_id = emp_id
        super().__init__(f"❌ Không tìm thấy nhân viên có ID: {emp_id}")


# =========================
# LƯƠNG KHÔNG HỢP LỆ
# =========================
class InvalidSalaryError(EmployeeException):
    def __init__(self, message="❌ Lương phải lớn hơn 0"):
        super().__init__(message)


# =========================
# TUỔI KHÔNG HỢP LỆ
# =========================
class InvalidAgeError(EmployeeException):
    def __init__(self, message="❌ Tuổi phải từ 18 đến 65"):
        super().__init__(message)


# =========================
# PHÂN CÔNG DỰ ÁN LỖI
# =========================
class ProjectAllocationError(EmployeeException):
    def __init__(self, message="❌ Không thể phân công dự án"):
        super().__init__(message)


# =========================
# TRÙNG NHÂN VIÊN
# =========================
class DuplicateEmployeeError(EmployeeException):
    def __init__(self, message="❌ Nhân viên đã tồn tại (trùng ID)"):
        super().__init__(message)