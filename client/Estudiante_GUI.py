import tkinter as tk
from tkinter import ttk, messagebox
from model.consultas import Estudiante, listar_ETDT

#--------------------- CONTENEDOR DE OBJETOS ESTUDIANTE ---------------------#
class Contenedor_Etdt_View(tk.Frame):
    def __init__(self, win_etdt = None):
        super().__init__(win_etdt, width=480, height=320)
        self.win_etdt = win_etdt
        self.pack()
        self.config(background='#009193')
        self.App_Estudiante_View()

    def App_Estudiante_View(self):

        self.label_nombre_pfsr = tk.Label(self, text = "ESTUDIANTES:")
        self.label_nombre_pfsr.config(fg="#FFFFFF", background="#009193", font= ("Arial",20," bold"))
        self.label_nombre_pfsr.grid(row=0, column=0, padx=10, pady=10)

        self.lista_estudiante = listar_ETDT()
        self.lista_estudiante.reverse()
        self.tabla = ttk.Treeview(self, columns= ("Nombre", "Apellido", "Asignatura", "Calificacion"))    
        
        self.tabla.grid(
            row=7,
            column=0, columnspan=6,
            sticky="nse"
        )

        self.scroll = ttk.Scrollbar(self, orient= "vertical", command=self.tabla.yview)
        self.tabla.config(yscrollcommand = self.scroll.set)

        self.scroll.grid(
            row=7,
            column=6,
            sticky="nse"
        )

        self.tabla.heading("#1", text="Nombre")
        self.tabla.heading("#2", text="Apellido")
        self.tabla.heading("#3", text="Asignatura")
        self.tabla.heading("#4", text="Calificacion")


        for p in self.lista_estudiante:
            self.tabla.insert('',0, text=p[0],
            values=(p[1], p[2], p[3], p[4]))


#-------------------------------- FUNCIONES GLOBALES------------------------------------#

#--- FUNCION DE MENU INICIO ---
def Bar_Menu_Etdt_view(win_etdt):
    barra_menu = tk.Menu(win_etdt)
    win_etdt.config(menu = barra_menu, width=300, height=300)

    #---- BOTONES-----
    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Inicio", menu= menu_inicio)

    menu_inicio.add_command(label="Crear base de datos")
    menu_inicio.add_command(label="Eliminar base de datos")
    menu_inicio.add_command(label="Salir", command= win_etdt.destroy)

    menu_consultar = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Consultar", menu= menu_consultar)


    barra_menu.add_cascade(label="Configuracion",)
    barra_menu.add_cascade(label="Ayuda",)