import customtkinter as ctk
from tkinter import ttk
import csv
import os

def load():
    table.delete(*table.get_children())
    if os.path.exists("data.csv"):
        with open("data.csv", "r") as f:
            for row in csv.reader(f):
                table.insert("", "end", values=row)

def add():
    if e1.get() and e2.get():
        with open("data.csv", "a", newline="") as f:
            csv.writer(f).writerow([e1.get(), e2.get()])
        e1.delete(0, 'end')
        e2.delete(0, 'end')
        load()

app = ctk.CTk()
app.geometry("500x500")
app.title("Asset Manager")

e1 = ctk.CTkEntry(app, placeholder_text="ID")
e1.pack(pady=10)

e2 = ctk.CTkEntry(app, placeholder_text="Name")
e2.pack(pady=10)

ctk.CTkButton(app, text="Add Asset", command=add).pack(pady=10)

table = ttk.Treeview(app, columns=(1, 2), show="headings")
table.heading(1, text="Asset ID")
table.heading(2, text="Asset Name")
table.pack(pady=20, fill="both", expand=True)

load()
app.mainloop()