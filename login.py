import tkinter
from tkinter import messagebox
from get_user import get_user_data
from App_Pygrades import main

window = tkinter.Tk()
window.title("Inicio de sesión")
window.geometry('440x580')
window.configure(bg='#333333')

def login():

    username = username_entry.get()
    password = password_entry.get()

    userData = []
    userData = get_user_data(username,password)

    dataUser = userData[0][0]
    dataPass = userData[1][0]
    dataId = userData[2][0]
    dataIste = userData[3][0]

    isteacher:int = 0

    if(dataId <6):
            isteacher = 1

    if dataUser==username and dataPass==password:
        messagebox.showinfo(title="Login Success", message="Haz iniciado sesión correctamente.")
        if(isteacher == 1):
             main()   
    else:
        messagebox.showerror(title="Error", message="Fallo en inicio de sesión.")

frame = tkinter.Frame(bg='#333333')

# Creating widgets
login_label = tkinter.Label(
    frame, text="Inicio de sesión", bg='#333333', fg="#3393FF", font=("Times New Roman", 30))
username_label = tkinter.Label(
    frame, text="Usuario", bg='#333333', fg="#FFFFFF", font=("Times New Roman", 16))
username_entry = tkinter.Entry(frame, font=("Arial", 16))
password_entry = tkinter.Entry(frame, show="*", font=("Times New Roman", 16))
password_label = tkinter.Label(
    frame, text="Contraseña", bg='#333333', fg="#FFFFFF", font=("Times New Roman", 16))
login_button = tkinter.Button(
    frame, text="Inicia sesión", bg="#3393FF", fg="#FFFFFF", font=("Times New Roman", 16), command=login)

# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()

window.mainloop()