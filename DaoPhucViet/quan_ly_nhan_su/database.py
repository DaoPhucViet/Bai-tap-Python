import sqlite3

def connect_db():
    conn = sqlite3.connect("nhansu.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS nhansu (
            cccd TEXT PRIMARY KEY,
            hoten TEXT,
            ngaysinh TEXT,
            gioitinh TEXT,
            diachi TEXT
        )
    """)
    return conn