import tkinter as tk
from tkinter import ttk
from model.consultas import listar_estd

#--------------------- CONTENEDOR DE OBJETOS ESTUDIANTE ---------------------#
class Contenedor_Etdt(tk.Frame):
    def __init__(self, win_etdt = None):
        super().__init__(win_etdt, width=480, height=320)
        self.win_etdt = win_etdt
        self.pack()
        self.config(background='#009193')
        self.App_Estudiante()
        self.view_student()

    def App_Estudiante(self):

        #BOTON DE SALIR
        self.boton_salir = tk.Button(self, text="Salir",command= self.btn_salir)
        self.boton_salir.config(
            width=20,
            font= ("Arial",12,"bold"),
            fg="#FFFFFF",
            background="#9F0000",
            cursor="hand2",
            activebackground="#DF0000",
            activeforeground="#FFFFFF"
            )
        
        self.boton_salir.grid(
            row=6,
            column=0,
            padx=10,
            pady=10,
        )

#-------------------------------- FUNCIONES CLASS Contenedor_etdt ------------------------------------#

    #--- FUNCION PARA BOTON SALIR ---
    def btn_salir(self):
            
        self.win_etdt.destroy


    #--- FUNCION VISTA ---
    def view_student(self):

        self.nameEst = 'Gabriela Camilo'
        self.lista_student = listar_estd(self.nameEst)
        self.lista_student.reverse()

        self.tabla = ttk.Treeview(self, columns = ("Nombre", "Asinatura", "Calificación", "Usuario","Contraseña" ))    
        
        self.tabla.grid(row = 6, column = 0, columnspan = 4, sticky = "nse")

        self.scroll = ttk.Scrollbar(self,
            orient="vertical", command= self.tabla.yview)
        self.scroll.grid( row = 6, column = 5, sticky = 'nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading("#0", text="ID")
        self.tabla.heading("#1", text="Nombre")
        self.tabla.heading("#2", text="Asinatura")
        self.tabla.heading("#3", text="Calificación")
        self.tabla.heading("#4", text="Usuario")
        self.tabla.heading("#5", text="Contraseña") 
        
        #
        for estd in self.lista_student:
            self.tabla.insert('',0, text=estd[0], 
                values=(estd[2],estd[5],estd[6],estd[3],estd[4]))
            self.config(padx=10, pady=10)


#-------------------------------- FUNCIONES GLOBALES------------------------------------#


#--- FUNCION DE MENU INICIO ---
def Bar_Menu_Etdt(win_esdt):
    barra_menu = tk.Menu(win_esdt)
    win_esdt.config(menu = barra_menu, width=300, height=300)

    #---- BOTONES-----
    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Inicio", menu= menu_inicio)

    menu_inicio.add_command(label="Salir", command= win_esdt.destroy)

    menu_consultar = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Consultar", menu= menu_consultar)


    barra_menu.add_cascade(label="Configuracion",)
    barra_menu.add_cascade(label="Ayuda",)