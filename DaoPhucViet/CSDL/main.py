import pyodbc

# ================= KẾT NỐI =================
def connect_db():
    try:
        conn = pyodbc.connect(
            r"DRIVER={ODBC Driver 17 for SQL Server};"
            r"SERVER=np:\\.\pipe\LOCALDB#C2F94373\tsql\query;"
            r"DATABASE=CompanyDB;"
            r"Trusted_Connection=yes;"
        )
        return conn
    except Exception as e:
        print("❌ Lỗi kết nối:", e)
        return None


# ================= MENU =================
def menu():
    print("\n========== MENU ==========")
    print("A. Xem danh sách MANAGER")
    print("B. Thêm phòng ban")
    print("C. Thêm nhân viên (bạn)")
    print("D. Cập nhật CLARK thành bạn")
    print("E. Xóa MILLER")
    print("0. Thoát")
    print("==========================")

# ================= A =================
def cau_A(cursor):
    print("\n📌 DANH SÁCH MANAGER:")
    cursor.execute("SELECT * FROM employee WHERE job = ?", ('MANAGER',))
    rows = cursor.fetchall()
    if rows:
        for r in rows:
            print(r)
    else:
        print("Không có dữ liệu.")

# ================= B =================
def cau_B(cursor, conn):
    try:
        deptno = int(input("Nhập mã phòng (vd: 50): "))
        dname = input("Nhập tên phòng: ")
        loc = input("Nhập địa điểm: ")

        cursor.execute(
            "INSERT INTO department VALUES (?, ?, ?)",
            (deptno, dname, loc)
        )
        conn.commit()
        print("✅ Thêm phòng ban thành công!")
    except Exception as e:
        print("❌ Lỗi:", e)

# ================= C =================
def cau_C(cursor, conn):
    try:
        empno = int(input("Mã NV: "))
        ename = input("Tên: ")
        job = input("Chức vụ: ")
        mgr = input("Manager (Enter nếu không có): ")
        mgr = int(mgr) if mgr else None
        hiredate = input("Ngày vào (YYYY-MM-DD): ")
        sal = float(input("Lương: "))
        comm = input("Hoa hồng (Enter nếu không): ")
        comm = float(comm) if comm else None
        deptno = int(input("Mã phòng: "))

        cursor.execute(
            "INSERT INTO employee VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (empno, ename, job, mgr, hiredate, sal, comm, deptno)
        )
        conn.commit()
        print("✅ Thêm nhân viên thành công!")
    except Exception as e:
        print("❌ Lỗi:", e)

# ================= D =================
def cau_D(cursor, conn):
    try:
        ename = input("Tên mới: ")
        job = input("Chức vụ mới: ")
        sal = float(input("Lương mới: "))

        cursor.execute(
            "UPDATE employee SET ename=?, job=?, sal=? WHERE ename=?",
            (ename, job, sal, 'CLARK')
        )
        conn.commit()
        print("✅ Đã cập nhật CLARK!")
    except Exception as e:
        print("❌ Lỗi:", e)

# ================= E =================
def cau_E(cursor, conn):
    try:
        cursor.execute(
            "DELETE FROM employee WHERE ename=?",
            ('MILLER',)
        )
        conn.commit()
        print("✅ Đã xóa MILLER!")
    except Exception as e:
        print("❌ Lỗi:", e)

# ================= MAIN =================
def main():
    conn = connect_db()
    if not conn:
        return

    cursor = conn.cursor()

    while True:
        menu()
        choice = input("Chọn: ").upper()

        if choice == 'A':
            cau_A(cursor)
        elif choice == 'B':
            cau_B(cursor, conn)
        elif choice == 'C':
            cau_C(cursor, conn)
        elif choice == 'D':
            cau_D(cursor, conn)
        elif choice == 'E':
            cau_E(cursor, conn)
        elif choice == '0':
            print("Thoát chương trình.")
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")

    conn.close()


if __name__ == "__main__":
    main()