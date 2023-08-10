import tkinter as tk
from tkinter import ttk, messagebox
from model.consultas import crear_tabla, borrar_tabla, Profesor, listar_PFSR, editar_PFSR, guardar_PFSR, eliminar_PFSR

#--------------------- CONTENEDOR DE OBJETOS PROFESOR ---------------------#
class Contenedor_Admn(tk.Frame):
    def __init__(self, win_admn):
        super().__init__(win_admn, width=480, height=320)
        self.win_admn = win_admn
        self.pack()
        self.config(background='#009193')
        self.ID_Profesor = None
        self.App_Administrador()
        self.deshabilitar_campos()
        self.view()

    def App_Administrador(self):


        # TEXTO DE CADA CAMPO
        self.label_nombre_pfsr = tk.Label(self, text = "Nombre:")
        self.label_nombre_pfsr.config(fg="#FFFFFF", background="#009193", font= ("Arial",12," bold"))
        self.label_nombre_pfsr.grid(row=0, column=0, padx=10, pady=10)

        self.label_Apellido_pfsr = tk.Label(self, text = "Apellido:")
        self.label_Apellido_pfsr.config(fg="#FFFFFF", background="#009193", font= ("Arial",12," bold"))
        self.label_Apellido_pfsr.grid(row=1, column=0, padx=10, pady=10)

        self.label_Asignatura_pfsr = tk.Label(self, text = "Asignatura:")
        self.label_Asignatura_pfsr.config(fg="#FFFFFF", background="#009193", font= ("Arial",12," bold"))
        self.label_Asignatura_pfsr.grid(row=2, column=0, padx=10, pady=10)

        self.label_Usuario_pfsr = tk.Label(self, text = "Usuario:")
        self.label_Usuario_pfsr.config(fg="#FFFFFF", background="#009193", font= ("Arial",12," bold"))
        self.label_Usuario_pfsr.grid(row=3, column=0, padx=10, pady=10)

        self.label_Contraseña_pfsr = tk.Label(self, text = "Contraseña:")
        self.label_Contraseña_pfsr.config(fg="#FFFFFF", background="#009193", font= ("Arial",12," bold"))
        self.label_Contraseña_pfsr.grid(row=4, column=0, padx=10, pady=10)


        # TEXTBOX (IMPUT) NOMBRE
        self.nombre_pfsr = tk.StringVar()
        self.entry_nombre_pfsr = tk.Entry(self, textvariable= self.nombre_pfsr)
        self.entry_nombre_pfsr.config(
            width=75,
            font= ("Arial",12)
            )
                    
        self.entry_nombre_pfsr.grid(
            row=0,
            column=1,
            padx=10,
            pady=10,
            columnspan=2
            )

        # TEXTBOX (IMPUT) APELLIDO
        self.apellido_pfsr = tk.StringVar()
        self.entry_apellido_pfsr = tk.Entry(self, textvariable= self.apellido_pfsr)
        self.entry_apellido_pfsr.config(
            width=75,
            font= ("Arial",12)
            )
        
        self.entry_apellido_pfsr.grid(
            row=1,
            column=1,
            padx=10,
            pady=10,
            columnspan=2
            )

        # TEXTBOX (IMPUT) ASIGNATURA
        self.asignatura_pfsr = tk.StringVar()
        self.entry_asignatura_pfsr = tk.Entry(self, textvariable= self.asignatura_pfsr)
        self.entry_asignatura_pfsr.config(
            width=75,
            font= ("Arial",12)  
            )
        
        self.entry_asignatura_pfsr.grid(
            row=2,
            column=1, 
            padx=10,
            pady=10,
            columnspan=2
            )
        
        # TEXTBOX (IMPUT) USUARIO
        self.usuario_pfsr = tk.StringVar()
        self.entry_usuario_pfsr = tk.Entry(self, textvariable= self.usuario_pfsr)
        self.entry_usuario_pfsr.config(
            width=75,
            font= ("Arial",12)  
            )
        
        self.entry_usuario_pfsr.grid(
            row=3,
            column=1, 
            padx=10,
            pady=10,
            columnspan=2
            )

        # TEXTBOX (IMPUT) CONTRASEÑA
        self.contraseña_pfsr = tk.StringVar()
        self.entry_contraseña_pfsr = tk.Entry(self, textvariable= self.contraseña_pfsr)
        self.entry_contraseña_pfsr.config(
            width=75,
            font= ("Arial",12)  
            )
        
        self.entry_contraseña_pfsr.grid(
            row=4,
            column=1, 
            padx=10,
            pady=10,
            columnspan=2
            )

        #--------Botones---------
        
        #BOTON DE CREAR
        self.boton_crear = tk.Button(self, text="Crear", command= self.habilitar_campos)
        self.boton_crear.config(
            width=20,
            font= ("Arial",12,"bold"),
            fg="#FFFFFF",
            background="#028400",
            cursor="hand2",
            activebackground="#03B800",
            activeforeground="#FFFFFF"
            )
        
        self.boton_crear.grid(
            row=1,
            column=4
        )

        #BOTON DE EDITAR
        self.boton_editar = tk.Button(self, text="Editar", command= self.editar_datos)
        self.boton_editar.config(
            width=20,
            font= ("Arial",12,"bold"),
            fg="#FFFFFF",
            background="#BCC800",
            cursor="hand2",
            activebackground="#DCEA00",
            activeforeground="#FFFFFF"
            )
        
        self.boton_editar.grid(
            row=2,
            column=4
        )

        #BOTON DE ELIMINAR
        self.boton_eliminar = tk.Button(self, text="Eliminar", command= self.eliminar_datos)
        self.boton_eliminar.config(
            width=20,
            font= ("Arial",12,"bold"),
            fg="#FFFFFF",
            background="#9F0000",
            cursor="hand2",
            activebackground="#DF0000",
            activeforeground="#FFFFFF"
            )
        
        self.boton_eliminar.grid(
            row=3,
            column=4
        )


        #BOTON DE GUARDAR
        self.boton_guardar = tk.Button(self, text="Guardar", command= self.guardar_datos)
        self.boton_guardar.config(
            width=20,
            font= ("Arial",12,"bold"),
            fg="#FFFFFF",
            background="#004ABD",
            cursor="hand2",
            activebackground="#005CE9",
            activeforeground="#FFFFFF"
            )
        
        self.boton_guardar.grid(
            row=7,
            column=4,
            padx=10,
            pady=10,
        )

        #BOTON DE SALIR
        self.boton_salir = tk.Button(self, text="Salir")
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
            row=7,
            column=0,
            padx=10,
            pady=10,
        )

#-------------------------------- FUNCIONES CLASS Contenedor_pfsr ------------------------------------#


    #--- FUNCION PARA HABILITAR LA ENTRADA DE TEXTO 
    def habilitar_campos(self):
        self.nombre_pfsr.set("")
        self.apellido_pfsr.set("")
        self.asignatura_pfsr.set("")
        self.usuario_pfsr.set("")
        self.contraseña_pfsr.set("")

        self.entry_nombre_pfsr.config(state="normal")
        self.entry_apellido_pfsr.config(state="normal")
        self.entry_asignatura_pfsr.config(state="normal")
        self.entry_usuario_pfsr.config(state="normal")
        self.entry_contraseña_pfsr.config(state="normal")

        self.boton_guardar.config(state="normal")

    #--- FUNCION PARA DESABILITAR LA ENTRADA DE TEXTO ---
    def deshabilitar_campos(self):
        self.nombre_pfsr.set("")
        self.apellido_pfsr.set("")
        self.asignatura_pfsr.set("")
        self.usuario_pfsr.set("")
        self.contraseña_pfsr.set("")

        self.entry_nombre_pfsr.config(state="disabled")
        self.entry_apellido_pfsr.config(state="disabled")
        self.entry_asignatura_pfsr.config(state="disabled")
        self.entry_usuario_pfsr.config(state="disabled")
        self.entry_contraseña_pfsr.config(state="disabled")

        self.boton_guardar.config(state="disabled")

   #----- GUARDAR DATOS  ------
    def guardar_datos(self):

        profesor = Profesor(
            self.nombre_pfsr.get(),
            self.apellido_pfsr.get(),
            self.asignatura_pfsr.get(),
            self.usuario_pfsr.get(),
            self.contraseña_pfsr.get(),
        )
        
        if self.ID_Profesor == None:
            guardar_PFSR(profesor)
        else:
            editar_PFSR(profesor, self.ID_Profesor)

        self.view()
        self.deshabilitar_campos()

    #----- VISTA DATOS --------
    def view (self):
        self.lista_profesor = listar_PFSR()
        self.lista_profesor.reverse()
        self.tabla = ttk.Treeview(self, columns= ("Nombre", "Apellido", "Asignatura", "Usuario", "Contraseña"))    
        
        self.tabla.grid(
            row=6,
            column=0, columnspan=5,
            sticky="nse"
        )

        self.scroll = ttk.Scrollbar(self, orient= "vertical", command=self.tabla.yview)
        self.tabla.config(yscrollcommand = self.scroll.set)

        self.scroll.grid(
            row=6,
            column=5,
            sticky="nse"
        )
 

        self.tabla.heading("#0", text="ID")
        self.tabla.heading("#1", text="Nombre")
        self.tabla.heading("#2", text="Apellido")
        self.tabla.heading("#3", text="Asignatura")
        self.tabla.heading("#4", text="Usuario")
        self.tabla.heading("#5", text="Contraseña")        

        for p in self.lista_profesor:
            self.tabla.insert('',0, text=p[0],
            values=(p[1], p[2], p[3], p[4], p[5]))

   #------ EDITAR DATOS -------
    def editar_datos(self):
        try:
            self.ID_Profesor = self.tabla.item(self.tabla.selection())["text"]
            self.Nombre_pfsr =self.tabla.item(
                self.tabla.selection())['values'][0]
            self.Apellido_pfsr =self.tabla.item(
                self.tabla.selection())['values'][1]
            self.Asignatura_pfsr =self.tabla.item(
                self.tabla.selection())['values'][2]
            self.Usuario_pfsr =self.tabla.item(
                self.tabla.selection())['values'][3]
            self.Contraseña_pfsr =self.tabla.item(
                self.tabla.selection())['values'][4]
            
            self.habilitar_campos()

            self.entry_nombre_pfsr.insert(0, self.Nombre_pfsr)
            self.entry_apellido_pfsr.insert(0, self.Apellido_pfsr)
            self.entry_asignatura_pfsr.insert(0, self.Asignatura_pfsr)
            self.entry_usuario_pfsr.insert(0, self.Usuario_pfsr)
            self.entry_contraseña_pfsr.insert(0, self.Contraseña_pfsr)

        except:
            titulo = "Edición de datos"
            menseje = "No ha seleccionado ningun registro"
            messagebox.showerror(titulo,menseje)

   #------ ELIMINAR DATOS------
    def eliminar_datos(self):

        try:
            self.ID_Profesor = self.tabla.item(self.tabla.selection())["text"]
            eliminar_PFSR(self.ID_Profesor)

            self.view()
        except:
            titulo = "Eliminar un Registro"
            menseje = "No se ha seleccionado ningun registro"
            messagebox.showerror(titulo,menseje)






#-------------------------------- FUNCIONES GLOBALES------------------------------------#


#--- FUNCION DE MENU INICIO ---
def Bar_Menu_ADMN(win_admn):
    barra_menu = tk.Menu(win_admn)
    win_admn.config(menu = barra_menu, width=300, height=300)

    #---- BOTONES -----
    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Inicio", menu= menu_inicio)

    menu_inicio.add_command(label="Crear base de datos", command= crear_tabla)
    menu_inicio.add_command(label="Eliminar base de datos", command= borrar_tabla)
    menu_inicio.add_command(label="Salir", command= win_admn.destroy)

    menu_consultar = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Consultar", menu= menu_consultar)


    barra_menu.add_cascade(label="Configuracion",)
    barra_menu.add_cascade(label="Ayuda",)