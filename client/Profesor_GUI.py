import tkinter as tk

class Contenedor_Pfsr(tk.Frame):
    def __init__(self, win_pfsr = None):
        super().__init__(win_pfsr, width=480, height=320, background='#009193')
        self.win_admn = win_pfsr
        self.pack()