import tkinter as tk
from tkinter import ttk, messagebox
from model.consultas import crear_tabla, borrar_tabla
from model.consultas import Students, guardar, listar, editar, eliminar

#--------------------- CONTENEDOR DE OBJETOS PROFESOR ---------------------#
class Contenedor_Pfsr(tk.Frame):
    def __init__(self, win_pfsr = None):
        super().__init__(win_pfsr, width=480, height=320)
        self.win_pfsr = win_pfsr
        self.config( background='#009193')
        self.pack()
        
        self.id_student = None

        self.App_Profesor()
        self.deshabilitar_campos()
        self.view_students()        

    def App_Profesor(self):

        # TEXTO DE CADA CAMPO
        self.label_nombre_estd = tk.Label(self, text = "Nombre:")
        self.label_nombre_estd.config(fg="#FFFFFF", background="#009193", font= ("Arial",12," bold"))
        self.label_nombre_estd.grid(row=0, column=0, padx=10, pady=10)

        self.label_asignatura_estd = tk.Label(self, text = "Asignatura:")
        self.label_asignatura_estd.config(fg="#FFFFFF", background="#009193", font= ("Arial",12," bold"))
        self.label_asignatura_estd.grid(row=1, column=0, padx=10, pady=10)

        self.label_calificacion_estd = tk.Label(self, text = "Calificación:")
        self.label_calificacion_estd.config(fg="#FFFFFF", background="#009193", font= ("Arial",12," bold"))
        self.label_calificacion_estd.grid(row=2, column=0, padx=10, pady=10)


        # TEXTBOX (IMPUT) NOMBRE
        self.nombre_estd = tk.StringVar()
        self.entry_nombre_estd = tk.Entry(self, textvariable= self.nombre_estd)
        self.entry_nombre_estd.config(width=50,font= ("Arial",12))
                    
        self.entry_nombre_estd.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

        # TEXTBOX (IMPUT) ASIGNATURA
        self.asignatura_estd = tk.StringVar()
        self.entry_asignatura_estd = tk.Entry(self, textvariable= self.asignatura_estd)
        self.entry_asignatura_estd.config(width=50, font= ("Arial",12))
        
        self.entry_asignatura_estd.grid(row=1, column=1,  padx=10, pady=10, columnspan=2)
        
        # TEXTBOX (IMPUT) CALIFICACIÓN
        self.calificacion_estd = tk.StringVar()
        self.entry_calificacion_estd = tk.Entry(self, textvariable= self.calificacion_estd)
        self.entry_calificacion_estd.config( width=50, font= ("Arial",12))
        
        self.entry_calificacion_estd.grid(row=2, column=1,  padx=10, pady=10, columnspan=2)

        #--------Botones---------
        
        #BOTON DE CREAR
        self.boton_crear = tk.Button(self, text="Crear", command= self.habilitar_campos)
        self.boton_crear.config( width=20, font= ("Arial",12,"bold"), fg="#FFFFFF", background="#028400", cursor="hand2",
            activebackground="#03B800",
            activeforeground="#FFFFFF"
            )
        
        self.boton_crear.grid( row=5, column=0, padx=10, pady=10)

        #BOTON DE CANCELAR
        self.boton_cancelar = tk.Button(self, text="Cancelar", command= self.deshabilitar_campos)
        self.boton_cancelar.config( width=20, font= ("Arial",12,"bold"), fg="#FFFFFF", background="#9F0000", cursor="hand2",
            activebackground="#DF0000",
            activeforeground="#FFFFFF"
            )
        
        self.boton_cancelar.grid( row=5, column=1, padx=10, pady=10)

        #BOTON DE GUARDAR
        self.boton_guardar = tk.Button(self, text="Guardar", command= self.guardar_datos)
        self.boton_guardar.config( width=20, font= ("Arial",12,"bold"), fg="#FFFFFF", background="#004ABD", cursor="hand2",
            activebackground="#005CE9",
            activeforeground="#FFFFFF"
            )
        
        self.boton_guardar.grid( row=5, column=2, padx=10, pady=10)

        #BOTON DE SALIR
        self.boton_salir = tk.Button(self, text="Salir",command= self.btn_salir)
        self.boton_salir.config( width=20, font= ("Arial",12,"bold"), fg="#FFFFFF", background="#9F0000", cursor="hand2",
            activebackground="#DF0000",
            activeforeground="#FFFFFF"
            )
        
        self.boton_salir.grid( row=7, column=0, padx=10, pady=10)

        #BOTON DE EDITAR
        self.boton_editar = tk.Button(self, text="Editar", command = self.editar_datos)
        self.boton_editar.config( width=20,font= ("Arial",12,"bold"), fg="#FFFFFF", background="#BCC800", cursor="hand2",
            activebackground="#DCEA00",
            activeforeground="#FFFFFF"
            )
        
        self.boton_editar.grid( row=7, column=1, padx=10, pady=10)

        #BOTON DE ELIMINAR
        self.boton_eliminar = tk.Button(self, text="Eliminar", command=self.eliminar_datos)
        self.boton_eliminar.config( width=20, font= ("Arial",12,"bold"), fg="#FFFFFF", background="#9F0000", cursor="hand2",
            activebackground="#DF0000",
            activeforeground="#FFFFFF"
            )
        
        self.boton_eliminar.grid( row=7, column=2, padx=10, pady=10)

#-------------------------------- FUNCIONES CLASS Contenedor_pfsr ------------------------------------#

    #--- FUNCION PARA HABILITAR LA ENTRADA DE TEXTO 
    def habilitar_campos(self):

        self.nombre_estd.set("")
        self.asignatura_estd.set("")
        self.calificacion_estd.set("")

        self.entry_nombre_estd.config(state="normal")
        self.entry_asignatura_estd.config(state="normal")
        self.entry_calificacion_estd.config(state="normal")

        self.boton_guardar.config(state="normal")
        self.boton_cancelar.config(state="normal")

    #--- FUNCION PARA DESABILITAR LA ENTRADA DE TEXTO ---
    def deshabilitar_campos(self):

        self.nombre_estd.set("")
        self.asignatura_estd.set("")
        self.calificacion_estd.set("")
        
        self.entry_nombre_estd.config(state="disabled")
        self.entry_asignatura_estd.config(state="disabled")
        self.entry_calificacion_estd.config(state="disabled")

        self.boton_guardar.config(state="disabled")
        self.boton_cancelar.config(state="disabled")

    #--- FUNCION PARA BOTON SALIR ---
    def btn_salir(self):
            
        self.win_pfsr.destroy()

    #--- FUNCION PARA GUARDAR DATOS ---
    def guardar_datos(self):
        
        student = Students(
            self.nombre_estd.get(),
            self.asignatura_estd.get(),
            self.calificacion_estd.get(),
        )

        if self.id_student == None:
            guardar(student)
        
        else :
            editar(student, self.id_student)

        self.view_students()

        self.deshabilitar_campos()

    #--- FUNCION VISTA DE ESTUDIANTES ---
    def view_students (self):

        self.lista_students = listar()
        self.lista_students.reverse()

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
        for estd in self.lista_students:
            self.tabla.insert('',0, text=estd[0], 
                values=(estd[2],estd[5],estd[6],estd[3],estd[4]))
            self.config(padx=10, pady=10)

    def editar_datos(self):
        #
            self.id_student = self.tabla.item(self.tabla.selection())["text"]
            self.nombre_estd_edit = self.tabla.item(self.tabla.selection())["values"][0]
            self.asignatura_estd_edit = self.tabla.item(self.tabla.selection())["values"][1]
            self.calificacion_estd_edit = self.tabla.item(self.tabla.selection())["values"][2]

            self.habilitar_campos()

            self.entry_nombre_estd.insert(0, self.nombre_estd_edit)
            self.entry_asignatura_estd.insert(0, self.asignatura_estd_edit)
            self.entry_calificacion_estd.insert(0, self.calificacion_estd_edit)

        #
    def eliminar_datos(self):
        self.id_student = self.tabla.item(self.tabla.selection())["text"]
        eliminar(self.id_student)
        self.view_students()

#-------------------------------- FUNCIONES GLOBALES------------------------------------#


#--- FUNCION DE MENU INICIO ---
def Bar_Menu_Pfsr(win_pfsr):
    barra_menu = tk.Menu(win_pfsr)
    win_pfsr.config(menu = barra_menu, width=300, height=300)

    #---- BOTONES -----
    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Inicio", menu= menu_inicio)

    menu_inicio.add_command(label="Crear base de datos", command= crear_tabla)
    menu_inicio.add_command(label="Eliminar base de datos", command= borrar_tabla)
    menu_inicio.add_command(label="Salir", command= win_pfsr.destroy)

    menu_consultar = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Consultar", menu= menu_consultar)

    barra_menu.add_cascade(label="Configuración",)
    barra_menu.add_cascade(label="Ayuda",)