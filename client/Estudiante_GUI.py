import tkinter as tk

class Contenedor_Esdt(tk.Frame):
    def __init__(self, win_esdt = None):
        super().__init__(win_esdt, width=480, height=320, background='#009193')
        self.win_admn = win_esdt
        self.pack()