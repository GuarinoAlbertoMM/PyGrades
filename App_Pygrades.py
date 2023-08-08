import tkinter as tk
from client.Administrador_GUI import Contenedor_Admn
from client.Profesor_GUI import Contenedor_Pfsr
from client.Estudiante_GUI import Contenedor_Esdt


# -------------------- VENTANAS --------------------- #

#---- ADMINISTRADOR -----
def Admn():
    win_admn = tk.Tk()
    win_admn.title ("Pygrades_Administrador")
    win_admn.iconbitmap("IMG/Logo_icono.ico")
    win_admn.resizable(0,0)

    app_admn = Contenedor_Admn(win_admn = win_admn)

    app_admn.mainloop()


#---- PROFESOR --------
def Pfsr():
    win_pfsr = tk.Tk()
    win_pfsr.title ("Pygrades_Profesor")
    win_pfsr.iconbitmap("IMG/Logo_icono.ico")
    win_pfsr.resizable(0,0)

    app_pfsr = Contenedor_Pfsr(win_pfsr = win_pfsr)

    app_pfsr.mainloop()

#---- ESTUDIANTE ------
def Etdt():
    win_esdt = tk.Tk()
    win_esdt.title ("Pygrades_Estudiante")
    win_esdt.iconbitmap("IMG/Logo_icono.ico")
    win_esdt.resizable(0,0)

    app_esdt = Contenedor_Esdt(win_esdt = win_esdt)

    app_esdt.mainloop()
    

if __name__ == '__main__':
    Admn()
    Pfsr()
    Etdt()