import tkinter as tk
from tkinter import messagebox

def login():
    username =username_entry.get()
    password = password_entry.get()
    print(username, password)
    if username == "aryan" and password == "12345678":
        messagebox.showinfo("Login Successful")
    else:
        messagebox.showerror("Invalid credentials")
parent = tk.Tk()
parent.geometry("450x400")
parent.title("Login form")

username_lbl = tk.Label(parent, text = "Username")
username_lbl.place(x = 10, y = 30)
username_entry = tk.Entry(parent)
username_entry.place(x = 80, y = 30)

password_labl = tk.Label(parent, text="Password")
password_labl.place(x = 10, y = 60)
password_entry = tk.Entry(parent, show='*')
password_entry.place(x = 80, y = 60)

login_btn = tk.Button(parent, text="Login", command=login)
login_btn.place(x=100, y=100)
parent.mainloop()