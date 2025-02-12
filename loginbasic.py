import tkinter as tk
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()
user_is_login = False
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
)
''')
conn.commit()

main = tk.Tk()
main.title("Menu Principal")
main.geometry("300x200")

admin = tk.Toplevel(main)
admin.title("AdminPanel")
admin.geometry("300x150")
admin.withdraw()

addUser = tk.Toplevel(main)
addUser.title("Adicionar Usuário")
addUser.geometry("300x200")
addUser.withdraw()
def seeAddUser():
    addUser.deiconify()

def login():
    email = login_email_entry.get()
    password = login_password_entry.get()
    if email and password:
        cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
        user = cursor.fetchone()
        if user:
            print("Logado")
            user_is_login = True
            admin.deiconify()
            main.withdraw()
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
        else:
            messagebox.showerror("Erro", "Email ou senha incorretos!")
def logout():
    user_is_login = False
    main.deiconify()
    addUser.withdraw()
    admin.withdraw()
def adicionar_usuario():
    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if username and email and password:
        cursor.execute("SELECT * FROM users WHERE username = ? OR email = ?", (username, email))
        user_exists = cursor.fetchone()
        if user_exists:
            messagebox.showerror("Erro", "Usuário ou email já cadastrado!")
        else:
            cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", 
                           (username, email, password))
            conn.commit()
            messagebox.showinfo("Sucesso", "Usuário adicionado com sucesso!")
            username_entry.delete(0, tk.END)
            email_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Erro", "Todos os campos são obrigatórios!")

username_label = tk.Label(addUser, text="Username")
username_entry = tk.Entry(addUser)
email_label = tk.Label(addUser, text="Email")
email_entry = tk.Entry(addUser)
password_label = tk.Label(addUser, text="Password")
password_entry = tk.Entry(addUser, show="*")
adduser_btn = tk.Button(addUser, text="Adicionar", command=adicionar_usuario)

login_email_label = tk.Label(main, text="Email")
login_email_entry = tk.Entry(main)
login_password_label = tk.Label(main, text="Password")
login_password_entry = tk.Entry(main, show="*")
login_btn = tk.Button(main, text="Login", command=login)
adduser_btn_admin = tk.Button(admin, text="AddUser", command=seeAddUser)

login_email_label.pack(pady=2)
login_email_entry.pack(pady=2)
login_password_label.pack(pady=2)
login_password_entry.pack(pady=2)
login_btn.pack(pady=5)

add_user_btn_admin = tk.Button(admin, text="Adicionar Usuarios", command=seeAddUser)
logout_btn = tk.Button(admin, text="Logout", command=logout)

username_label.pack(pady=2)
username_entry.pack(pady=2)
email_label.pack(pady=2)
email_entry.pack(pady=2)
password_label.pack(pady=2)
password_entry.pack(pady=2)
adduser_btn.pack(pady=5)

add_user_btn_admin.pack(pady=2)
logout_btn.pack(pady=2)
try:
    main.mainloop()
except KeyboardInterrupt:
    print("Programa Encerrado")
