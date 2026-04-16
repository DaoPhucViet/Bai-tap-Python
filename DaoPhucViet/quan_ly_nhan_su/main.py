import tkinter as tk
from tkinter import ttk, messagebox
from database import connect_db
import nhansu_service as service

conn = connect_db()

root = tk.Tk()
root.title("Quản lý nhân sự")
root.geometry("900x550")
root.configure(bg="#f5f6fa")

style = ttk.Style()
style.theme_use("clam")

# ===== STYLE =====
style.configure("Treeview",
                background="white",
                foreground="black",
                rowheight=28,
                fieldbackground="white")

style.configure("Treeview.Heading",
                font=("Segoe UI", 10, "bold"))

style.configure("TButton",
                font=("Segoe UI", 10),
                padding=6)

style.configure("TLabel",
                font=("Segoe UI", 10),
                background="#f5f6fa")

# ===== TITLE =====
title = tk.Label(root, text="QUẢN LÝ NHÂN SỰ",
                 font=("Segoe UI", 16, "bold"),
                 bg="#f5f6fa", fg="#2f3640")
title.pack(pady=10)

# ===== MAIN FRAME =====
main_frame = tk.Frame(root, bg="#f5f6fa")
main_frame.pack(fill="both", expand=True, padx=10)

# ===== FORM =====
form_frame = tk.LabelFrame(main_frame, text="Thông tin nhân sự",
                           font=("Segoe UI", 10, "bold"),
                           bg="#f5f6fa", padx=10, pady=10)
form_frame.pack(side="left", fill="y", padx=10)

labels = ["CCCD", "Họ tên", "Ngày sinh", "Giới tính", "Địa chỉ"]
entries = []

for i, text in enumerate(labels):
    ttk.Label(form_frame, text=text).grid(row=i, column=0, sticky="w", pady=5)
    e = ttk.Entry(form_frame, width=25)
    e.grid(row=i, column=1, pady=5)
    entries.append(e)

# ===== SEARCH =====
search_frame = tk.Frame(main_frame, bg="#f5f6fa")
search_frame.pack(fill="x", pady=5)

txtSearch = ttk.Entry(search_frame, width=30)
txtSearch.pack(side="left", padx=5)

# ===== TABLE =====
table_frame = tk.Frame(main_frame)
table_frame.pack(side="right", fill="both", expand=True)

cols = ("CCCD", "Họ tên", "Ngày sinh", "Giới tính", "Địa chỉ")
table = ttk.Treeview(table_frame, columns=cols, show="headings")

for col in cols:
    table.heading(col, text=col)
    table.column(col, anchor="center")

scroll = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
table.configure(yscroll=scroll.set)

table.pack(side="left", fill="both", expand=True)
scroll.pack(side="right", fill="y")

# ===== FUNCTIONS =====
def get_data():
    return tuple(e.get() for e in entries)

def load_data(data=None):
    for row in table.get_children():
        table.delete(row)

    rows = data if data else service.lay_ds(conn)
    for row in rows:
        table.insert("", "end", values=row)

def them():
    try:
        service.them(conn, get_data())
        load_data()
    except:
        messagebox.showerror("Lỗi", "CCCD bị trùng!")

def sua():
    service.sua(conn, get_data())
    load_data()

def xoa():
    cccd = entries[0].get()
    service.xoa(conn, cccd)
    load_data()

def tim():
    keyword = txtSearch.get()
    data = service.tim(conn, keyword)
    load_data(data)

def fill_data(event):
    selected = table.focus()
    values = table.item(selected, "values")
    if values:
        for i in range(len(entries)):
            entries[i].delete(0, tk.END)
            entries[i].insert(0, values[i])

table.bind("<<TreeviewSelect>>", fill_data)

# ===== BUTTONS =====
btn_frame = tk.Frame(root, bg="#f5f6fa")
btn_frame.pack(pady=10)

ttk.Button(btn_frame, text="➕ Thêm", command=them).grid(row=0, column=0, padx=5)
ttk.Button(btn_frame, text="✏️ Sửa", command=sua).grid(row=0, column=1, padx=5)
ttk.Button(btn_frame, text="🗑 Xóa", command=xoa).grid(row=0, column=2, padx=5)
ttk.Button(btn_frame, text="🔍 Tìm", command=tim).grid(row=0, column=3, padx=5)
ttk.Button(btn_frame, text="🔄 Làm mới", command=lambda: load_data()).grid(row=0, column=4, padx=5)

load_data()
root.mainloop()