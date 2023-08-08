import tkinter as tk

#--------------------- CONTENEDOR DE OBJETOS ADMINISTRADOR ---------------------#
class Contenedor_Admn(tk.Frame):
    def __init__(self, win_admn = None):
        super().__init__(win_admn, width=480, height=320, background='#009193')
        self.win_admn = win_admn
        self.pack()

#------------- FUNCIONES ------------
def barra_menu(win_admn):
    barra_menu = tk.Menu(win_admn)
    win_admn.config (menu = barra_menu, width = 300, height = 300)

