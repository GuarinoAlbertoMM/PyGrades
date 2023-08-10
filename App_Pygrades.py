import tkinter as tk
from client.Administrador_GUI import Contenedor_Admn, Bar_Menu_ADMN
from client.Profesor_GUI import Contenedor_Pfsr, Bar_Menu_Pfsr
from client.Estudiante_GUI import Contenedor_Etdt_View, Bar_Menu_Etdt_view


# -------------------- VENTANAS --------------------- #

#---- ADMINISTRADOR -----
def Admn():
    win_admn = tk.Tk()
    win_admn.title ("Pygrades_Administrador")
    win_admn.iconbitmap("IMG/Logo_icono.ico")
    win_admn.resizable(0,0)
    Bar_Menu_ADMN(win_admn)


    app_admn = Contenedor_Admn(win_admn = win_admn)

    app_admn.mainloop()

#---- PROFESOR --------
def Pfsr():
    win_pfsr = tk.Tk()
    win_pfsr.title ("Pygrades_Profesor")
    win_pfsr.iconbitmap("IMG/Logo_icono.ico")
    Bar_Menu_Pfsr(win_pfsr)
    win_pfsr.resizable(20,20)
    app_pfsr = Contenedor_Pfsr(win_pfsr = win_pfsr)

    app_pfsr.mainloop()

#---- ESTUDIANTE ------
def Etdt():
    win_etdt = tk.Tk()
    win_etdt.title ("Pygrades_Estudiante")
    win_etdt.iconbitmap("IMG/Logo_icono.ico")
    win_etdt.resizable(0,0)
    Bar_Menu_Etdt_view(win_etdt)
    app_etdt = Contenedor_Etdt_View(win_etdt = win_etdt)

    app_etdt.mainloop()
    

if __name__ == '__main__':
    Admn()
    Pfsr()
    Etdt()