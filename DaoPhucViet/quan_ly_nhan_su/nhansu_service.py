def them(conn, data):
    conn.execute("INSERT INTO nhansu VALUES (?, ?, ?, ?, ?)", data)
    conn.commit()

def sua(conn, data):
    conn.execute("""
        UPDATE nhansu 
        SET hoten=?, ngaysinh=?, gioitinh=?, diachi=?
        WHERE cccd=?
    """, (data[1], data[2], data[3], data[4], data[0]))
    conn.commit()

def xoa(conn, cccd):
    conn.execute("DELETE FROM nhansu WHERE cccd=?", (cccd,))
    conn.commit()

def lay_ds(conn):
    return conn.execute("SELECT * FROM nhansu").fetchall()

def tim(conn, keyword):
    return conn.execute("""
        SELECT * FROM nhansu
        WHERE cccd LIKE ? OR hoten LIKE ? OR diachi LIKE ?
    """, ('%'+keyword+'%', '%'+keyword+'%', '%'+keyword+'%')).fetchall()