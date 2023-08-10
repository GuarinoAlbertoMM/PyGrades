import tkinter as tk
from tkinter import ttk, messagebox
from model.consultas import crear_tabla, borrar_tabla, Estudiante, guardar_ETDT, listar_ETDT, editar_ETDT, eliminar_ETDT

#--------------------- CONTENEDOR DE OBJETOS ESTUDIANTE ---------------------#
class Contenedor_Pfsr(tk.Frame):
    def __init__(self, win_pfsr = None):
        super().__init__(win_pfsr, width=480, height=320)
        self.win_pfsr = win_pfsr
        self.pack()
        self.config(background='#009193')
        self.ID_Estudiante = None
        self.App_Profesor()
        self.deshabilitar_campos()
        self.view()

    def App_Profesor(self):

        # TEXTO DE CADA CAMPO
        self.label_nombre_etdt = tk.Label(self, text = "Nombre:")
        self.label_nombre_etdt.config(fg="#FFFFFF", background="#009193", font= ("Arial",12," bold"))
        self.label_nombre_etdt.grid(row=0, column=0, pady=10)

        self.label_Apellido_etdt = tk.Label(self, text = "Apellido:")
        self.label_Apellido_etdt.config(fg="#FFFFFF", background="#009193", font= ("Arial",12," bold"))
        self.label_Apellido_etdt.grid(row=1, column=0, pady=10)
        
        self.label_Edad_etdt = tk.Label(self, text = "Asignatura:")
        self.label_Edad_etdt.config(fg="#FFFFFF", background="#009193", font= ("Arial",12," bold"))
        self.label_Edad_etdt.grid(row=2, column=0, pady=10)

        self.label_Edad_etdt = tk.Label(self, text = "Calificacion:")
        self.label_Edad_etdt.config(fg="#FFFFFF", background="#009193", font= ("Arial",12," bold"))
        self.label_Edad_etdt.grid(row=3, column=0, pady=10)

        self.label_Usuario_etdt = tk.Label(self, text = "Usuario:")
        self.label_Usuario_etdt.config(fg="#FFFFFF", background="#009193", font= ("Arial",12," bold"))
        self.label_Usuario_etdt.grid(row=4, column=0, pady=10)

        self.label_Contraseña_etdt = tk.Label(self, text = "Contraseña:")
        self.label_Contraseña_etdt.config(fg="#FFFFFF", background="#009193", font= ("Arial",12," bold"))
        self.label_Contraseña_etdt.grid(row=5, column=0, pady=10)


        # TEXTBOX (IMPUT) NOMBRE
        self.nombre_etdt = tk.StringVar()
        self.entry_nombre_etdt = tk.Entry(self, textvariable= self.nombre_etdt)
        self.entry_nombre_etdt.config(
            width=75,
            font= ("Arial",12)
            )
                    
        self.entry_nombre_etdt.grid(
            row=0,
            column=1,
            columnspan=2
            )

        # TEXTBOX (IMPUT) APELLIDO
        self.apellido_etdt = tk.StringVar()
        self.entry_apellido_etdt = tk.Entry(self, textvariable= self.apellido_etdt)
        self.entry_apellido_etdt.config(
            width=75,
            font= ("Arial",12)
            )
        
        self.entry_apellido_etdt.grid(
            row=1,
            column=1,
            columnspan=2
            )
        
        # TEXTBOX (IMPUT) Asignatura
        self.asignatura_etdt = tk.StringVar()
        self.entry_asignatura_etdt = tk.Entry(self, textvariable= self.asignatura_etdt)
        self.entry_asignatura_etdt.config(
            width=75,
            font= ("Arial",12)
            )
        
        self.entry_asignatura_etdt.grid(
            row=2,
            column=1,
            columnspan=2
            )
        # TEXTBOX (IMPUT) CALIFICACION
        self.calificacion_etdt = tk.StringVar()
        self.entry_calificacion_etdt = tk.Entry(self, textvariable= self.calificacion_etdt)
        self.entry_calificacion_etdt.config(
            width=75,
            font= ("Arial",12)
            )
        
        self.entry_calificacion_etdt.grid(
            row=3,
            column=1,
            columnspan=2
            )

        
        # TEXTBOX (IMPUT) USUARIO
        self.usuario_etdt = tk.StringVar()
        self.entry_usuario_etdt = tk.Entry(self, textvariable= self.usuario_etdt)
        self.entry_usuario_etdt.config(
            width=75,
            font= ("Arial",12)  
            )
        
        self.entry_usuario_etdt.grid(
            row=4,
            column=1, 
            columnspan=2
            )

        # TEXTBOX (IMPUT) CONTRASEÑA
        self.contraseña_etdt = tk.StringVar()
        self.entry_contraseña_etdt = tk.Entry(self, textvariable= self.contraseña_etdt)
        self.entry_contraseña_etdt.config(
            width=75,
            font= ("Arial",12)  
            )
        
        self.entry_contraseña_etdt.grid(
            row=5,
            column=1, 
            columnspan=2
            )

        #--------Botones---------
        
        #BOTON DE CREAR
        self.boton_crear = tk.Button(self, text="Crear", command= self.habilitar_campos)
        self.boton_crear.config(
            width=25,
            font= ("Arial",12,"bold"),
            fg="#FFFFFF",
            background="#028400",
            cursor="hand2",
            activebackground="#03B800",
            activeforeground="#FFFFFF"
            )
        
        self.boton_crear.grid(
            row=1,
            column=4,
            padx=10,
            pady=10,
        )

        #BOTON DE EDITAR
        self.boton_editar = tk.Button(self, text="Editar", command= self.editar_datos)
        self.boton_editar.config(
            width=25,
            font= ("Arial",12,"bold"),
            fg="#FFFFFF",
            background="#BCC800",
            cursor="hand2",
            activebackground="#DCEA00",
            activeforeground="#FFFFFF"
            )
        
        self.boton_editar.grid(
            row=2,
            column=4,
            padx=10,
            pady=10,
        )

        #BOTON DE ELIMINAR
        self.boton_eliminar = tk.Button(self, text="Eliminar", command= self.eliminar_datos)
        self.boton_eliminar.config(
            width=25,
            font= ("Arial",12,"bold"),
            fg="#FFFFFF",
            background="#9F0000",
            cursor="hand2",
            activebackground="#DF0000",
            activeforeground="#FFFFFF"
            )
        
        self.boton_eliminar.grid(
            row=3,
            column=4,
            padx=10,
            pady=10,
        )


        #BOTON DE GUARDAR
        self.boton_guardar = tk.Button(self, text="Guardar", command= self.guardar_datos)
        self.boton_guardar.config(
            width=25,
            font= ("Arial",12,"bold"),
            fg="#FFFFFF",
            background="#004ABD",
            cursor="hand2",
            activebackground="#005CE9",
            activeforeground="#FFFFFF"
            )
        
        self.boton_guardar.grid(
            row=8,
            column=4,
            padx=10,
            pady=10,
        )

        #BOTON DE SALIR
        self.boton_salir = tk.Button(self, text="Salir")
        self.boton_salir.config(
            width=25,
            font= ("Arial",12,"bold"),
            fg="#FFFFFF",
            background="#9F0000",
            cursor="hand2",
            activebackground="#DF0000",
            activeforeground="#FFFFFF"
            )
        
        self.boton_salir.grid(
            row=8,
            column=0,
            padx=10,
            pady=10,
        )

#-------------------------------- FUNCIONES CLASS Contenedor_ETDT ------------------------------------#

    #--- FUNCION PARA HABILITAR LA ENTRADA DE TEXTO 
    def habilitar_campos(self):
        self.nombre_etdt.set("")
        self.apellido_etdt.set("")
        self.asignatura_etdt.set("")
        self.calificacion_etdt.set("")
        self.usuario_etdt.set("")
        self.contraseña_etdt.set("")
    
        self.entry_nombre_etdt.config(state="normal")
        self.entry_apellido_etdt.config(state="normal")
        self.entry_asignatura_etdt.config(state="normal")
        self.entry_calificacion_etdt.config(state="normal")
        self.entry_usuario_etdt.config(state="normal")
        self.entry_contraseña_etdt.config(state="normal")

        self.boton_guardar.config(state="normal")

    #--- FUNCION PARA DESABILITAR LA ENTRADA DE TEXTO ---
    def deshabilitar_campos(self):
        self.nombre_etdt.set("")
        self.apellido_etdt.set("")
        self.asignatura_etdt.set("")
        self.calificacion_etdt.set("")
        self.usuario_etdt.set("")
        self.contraseña_etdt.set("")
    
        self.entry_nombre_etdt.config(state="disabled")
        self.entry_apellido_etdt.config(state="disabled")
        self.entry_asignatura_etdt.config(state="disabled")
        self.entry_calificacion_etdt.config(state="disabled")
        self.entry_usuario_etdt.config(state="disabled")
        self.entry_contraseña_etdt.config(state="disabled")

        self.boton_guardar.config(state="disabled")

    #----- GUARDAR DATOS --------
    def guardar_datos(self):

        estudiante = Estudiante(
            self.nombre_etdt.get(),
            self.apellido_etdt.get(),
            self.asignatura_etdt.get(),
            self.calificacion_etdt.get(),
            self.usuario_etdt.get(),
            self.contraseña_etdt.get(),
        )
        
        if self.ID_Estudiante == None:
            guardar_ETDT(estudiante)
        else:
            editar_ETDT(estudiante, self.ID_Estudiante)

        self.view()
        self.deshabilitar_campos()

    #----- FUNCION VISTA --------
    def view (self):
        self.lista_estudiante = listar_ETDT()
        self.lista_estudiante.reverse()
        self.tabla = ttk.Treeview(self, columns= ("Nombre", "Apellido", "Asignatura", "Calificacion", "Usuario", "Contraseña"))    
        
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

        self.tabla.heading("#0", text="ID")
        self.tabla.heading("#1", text="Nombre")
        self.tabla.heading("#2", text="Apellido")
        self.tabla.heading("#3", text="Asignatura")
        self.tabla.heading("#4", text="Calificacion")
        self.tabla.heading("#5", text="Usuario")
        self.tabla.heading("#6", text="Contraseña")        

        for p in self.lista_estudiante:
            self.tabla.insert('',0, text=p[0],
            values=(p[1], p[2], p[3], p[4], p[5], p[6]))

    #----- EDITAR DATOS ---------
    def editar_datos(self):
        try:
            self.ID_Estudiante = self.tabla.item(self.tabla.selection())["text"]
            self.Nombre_etdt =self.tabla.item(
                self.tabla.selection())['values'][0]
            self.Apellido_etdt =self.tabla.item(
                self.tabla.selection())['values'][1]
            self.Asignatura_etdt =self.tabla.item(
                self.tabla.selection())['values'][2]
            self.Calificacion_etdt =self.tabla.item(
                self.tabla.selection())['values'][3]
            self.Usuario_etdt =self.tabla.item(
                self.tabla.selection())['values'][4]
            self.Contraseña_etdt =self.tabla.item(
                self.tabla.selection())['values'][5]
                        
            self.habilitar_campos()

            self.entry_nombre_etdt.insert(0, self.Nombre_etdt)
            self.entry_apellido_etdt.insert(0, self.Apellido_etdt)
            self.entry_asignatura_etdt.insert(0, self.Asignatura_etdt)
            self.entry_calificacion_etdt.insert(0, self.Calificacion_etdt)
            self.entry_usuario_etdt.insert(0, self.Usuario_etdt)
            self.entry_contraseña_etdt.insert(0, self.Contraseña_etdt)

        except:
            titulo = "Edición de datos"
            menseje = "No ha seleccionado ningun registro"
            messagebox.showerror(titulo,menseje)
    #----- ELIMINAR DATOS -------
    def eliminar_datos(self):

        try:
            self.ID_Estudiante = self.tabla.item(self.tabla.selection())["text"]
            eliminar_ETDT(self.ID_Estudiante)

            self.view()
        except:
            titulo = "Eliminar un Registro"
            menseje = "No se ha seleccionado ningun registro"
            messagebox.showerror(titulo,menseje)

#-------------------------------- FUNCIONES GLOBALES------------------------------------#

#--- FUNCION DE MENU INICIO ---
def Bar_Menu_Pfsr(win_win_pfsr):
    barra_menu = tk.Menu(win_win_pfsr)
    win_win_pfsr.config(menu = barra_menu, width=300, height=300)

    #---- BOTONES-----
    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Inicio", menu= menu_inicio)

    menu_inicio.add_command(label="Crear base de datos", command= crear_tabla)
    menu_inicio.add_command(label="Eliminar base de datos", command= borrar_tabla)
    menu_inicio.add_command(label="Salir", command= win_win_pfsr.destroy)

    menu_consultar = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Consultar", menu= menu_consultar)


    barra_menu.add_cascade(label="Configuracion",)
    barra_menu.add_cascade(label="Ayuda",)

    