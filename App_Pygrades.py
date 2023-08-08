import tkinter as tk
from client.Frame_GUI import Frame, barra_menu

def main():
    ventana = tk.Tk()
    ventana.title ("Pygrades")
    ventana.iconbitmap("IMG/Logo_icono.ico")
    ventana.resizable(0,0)
    barra_menu(ventana)
    app = Frame (ventana = ventana)

    app.mainloop()

if __name__ == '__main__':
    main()

    
