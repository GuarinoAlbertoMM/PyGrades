import tkinter as tk
from tkinter import ttk, messagebox

#--------------------- CONTENEDOR DE OBJETOS ADMINISTRADOR ---------------------#
class Contenedor_Admn(tk.Frame):
    def __init__(self, win_admn):
        super().__init__(win_admn, width=480, height=320)
        self.win_admn = win_admn
        self.pack()
        self.config(background='#009193')
        self.App_Administrador()
        self.deshabilitar_campos()
        self.view()

    def App_Administrador(self):

        # TEXTO DE CADA CAMPO
        self.label_nombre_admn = tk.Label(self, text = "Nombre:")
        self.label_nombre_admn.config(fg="#FFFFFF", background="#009193", font= ("Arial",12," bold"), width=25)
        self.label_nombre_admn.grid(row=0, column=0, padx=10, pady=10,)

        self.label_Apellido_admn = tk.Label(self, text = "Apellido:")
        self.label_Apellido_admn.config(fg="#FFFFFF", background="#009193", font= ("Arial",12," bold"))
        self.label_Apellido_admn.grid(row=1, column=0, padx=10, pady=10)

        self.label_Usuario_admn = tk.Label(self, text = "Usuario:")
        self.label_Usuario_admn.config(fg="#FFFFFF", background="#009193", font= ("Arial",12," bold"))
        self.label_Usuario_admn.grid(row=2, column=0, padx=10, pady=10)

        self.label_Contraseña_admn = tk.Label(self, text = "Contraseña:")
        self.label_Contraseña_admn.config(fg="#FFFFFF", background="#009193", font= ("Arial",12," bold"))
        self.label_Contraseña_admn.grid(row=3, column=0, padx=10, pady=10)

        # TEXTBOX (IMPUT) NOMBRE
        self.nombre_admn = tk.StringVar()
        self.entry_nombre_admn = tk.Entry(self, textvariable= self.nombre_admn)
        self.entry_nombre_admn.config(
            width=50,
            font= ("Arial",12),           
            )
                    
        self.entry_nombre_admn.grid(
            row=0,
            column=1,
            padx=20,
            pady=20,
            columnspan=3
            )

        # TEXTBOX (IMPUT) APELLIDO
        self.apellido_admn = tk.StringVar()
        self.entry_apellido_admn = tk.Entry(self, textvariable= self.apellido_admn)
        self.entry_apellido_admn.config(
            width=50,
            font= ("Arial",12)
            )
        
        self.entry_apellido_admn.grid(
            row=1,
            column=1,
            padx=20,
            pady=20,
            columnspan=3
            )
        
        # TEXTBOX (IMPUT) USUARIO
        self.usuario_admn = tk.StringVar()
        self.entry_usuario_admn = tk.Entry(self, textvariable= self.usuario_admn)
        self.entry_usuario_admn.config(
            width=50,
            font= ("Arial",12)  
            )
        
        self.entry_usuario_admn.grid(
            row=2,
            column=1, 
            padx=20,
            pady=20,
            columnspan=3
            )

        # TEXTBOX (IMPUT) CONTRASEÑA
        self.contraseña_admn = tk.StringVar()
        self.entry_contraseña_admn = tk.Entry(self, textvariable= self.contraseña_admn)
        self.entry_contraseña_admn.config(
            width=50,
            font= ("Arial",12),  
            
            )
        
        self.entry_contraseña_admn.grid(
            row=3,
            column=1, 
            padx=20,
            pady=20,
            columnspan=3
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
            row=4,
            column=2,
            padx=10,
            pady=10,
        )

        #BOTON DE EDITAR
        self.boton_editar = tk.Button(self, text="Editar")
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
            row=4,
            column=1,
            padx=10,
            pady=10,
        )

        #BOTON DE ELIMINAR
        self.boton_eliminar = tk.Button(self, text="Eliminar", command= self.deshabilitar_campos)
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
            row=4,
            column=0,
            padx=10,
            pady=10,
        )


        #BOTON DE GUARDAR
        self.boton_guardar = tk.Button(self, text="Guardar", command= self.deshabilitar_campos)
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
            row=6,
            column=2,
            padx=10,
            pady=10,
        )

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
    
#-------------------------------- FUNCIONES CLASS Contenedor_Admn ------------------------------------#


    #--- FUNCION PARA HABILITAR LA ENTRADA DE TEXTO 
    def habilitar_campos(self):
        self.nombre_admn.set("")
        self.apellido_admn.set("")
        self.usuario_admn.set("")
        self.contraseña_admn.set("")

        self.entry_nombre_admn.config(state="normal",background="#DCDCDC")
        self.entry_apellido_admn.config(state="normal",background="#DCDCDC")
        self.entry_usuario_admn.config(state="normal",background="#DCDCDC")
        self.entry_contraseña_admn.config(state="normal", background="#DCDCDC")

        self.boton_guardar.config(state="normal")
        self.boton_eliminar.config(state="normal")

    #--- FUNCION PARA DESABILITAR LA ENTRADA DE TEXTO ---
    def deshabilitar_campos(self):
        self.nombre_admn.set("")
        self.apellido_admn.set("")
        self.usuario_admn.set("")
        self.contraseña_admn.set("")

        self.entry_nombre_admn.config(state="disabled")
        self.entry_apellido_admn.config(state="disabled")
        self.entry_usuario_admn.config(state="disabled")
        self.entry_contraseña_admn.config(state="disabled")

        self.boton_guardar.config(state="disabled")
        self.boton_eliminar.config(state="disabled")

    #--- FUNCION PARA BOTON SALIR ---
    def btn_salir(self):
            
        self.win_admn.destroy

    #--- FUNCION PARA BOTON GUARDAR ---
    def guardar_datos(self):

        
        self.view()
        
        self.deshabilitar_campos()

    #--- FUNCION VISTA ---
    def view (self):

        self.tabla = ttk.Treeview(self, columns= ("Nombre", "Apellido", "Usuario", "Contraseña"))    
        
        self.tabla.grid(
            row=5,
            column=0, columnspan=4,
            sticky="nse"
        )

        self.tabla.heading("#0", text="ID")
        self.tabla.heading("#1", text="Nombre")
        self.tabla.heading("#2", text="Apellido")
        self.tabla.heading("#3", text="Usuario")
        self.tabla.heading("#4", text="Contraseña")        

        self.tabla.insert('',0, text="1", 
            values=("Alexander", "Agramonte", "Alex_A", "Gracias"))
        self.config(padx=10, pady=10)







#-------------------------------- FUNCIONES GLOBALES------------------------------------#

#--- FUNCION DE MENU INICIO ---
def Bar_Menu_Admn(win_admn):
    barra_menu = tk.Menu(win_admn)
    win_admn.config(menu = barra_menu, width=100, height=300)

    #---- BOTONES-----
    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Inicio", menu= menu_inicio)

    menu_inicio.add_command(label="Crear base de datos")
    menu_inicio.add_command(label="Eliminar base de datos")
    menu_inicio.add_command(label="Salir", command= win_admn.destroy)

    menu_consultar = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Consultar", menu= menu_consultar)


    barra_menu.add_cascade(label="Configuracion",)
    barra_menu.add_cascade(label="Ayuda",)
    
