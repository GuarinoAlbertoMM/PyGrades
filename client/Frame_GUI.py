import tkinter as tk
from tkinter import ttk
from model.consultas import crear_tabla, borrar_tabla, Pygrades, guardar, listar

#----- BARRA MENÚ ( HEAD ) --------
def barra_menu(ventana):
    barra_menu = tk.Menu(ventana)
    ventana.config(menu = barra_menu,
    width=300,
    height=300,
    )

    # OBJETO BARRA DE INICIO ( HEAD )
    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Inicio", menu= menu_inicio)

    menu_inicio.add_command(label="Crear base de datos", command= crear_tabla)
    menu_inicio.add_command(label="Eliminar base de datos", command= borrar_tabla)
    menu_inicio.add_command(label="Salir", command=ventana.destroy)

    menu_consultar = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="Consultar", menu= menu_consultar)


    barra_menu.add_cascade(label="Configuracion",)
    barra_menu.add_cascade(label="Ayuda",)

#--------- CUERPO CONTENEDOR ------------ 
class Frame(tk.Frame):
    def __init__(self, ventana = None):
        super().__init__(
            ventana, width= 480, height= 320,
            )
        self.ventana = ventana
        self.pack()
        self.config( background= "#292929" )
        self.App_Pygrades()
        self.deshabilitar_campos()
        self.view()

    def App_Pygrades (self):

        # TEXTO DE CADA CAMPO
        self.label_nombre = tk.Label(self, text = "Estudiante:")
        self.label_nombre.config(fg="#FFFFFF", background="#292929", font= ("Arial",12," bold"))
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)

        self.label_asignatura = tk.Label(self, text = "Asignatura:")
        self.label_asignatura.config(fg="#FFFFFF", background="#292929", font= ("Arial",12," bold"))
        self.label_asignatura.grid(row=1, column=0, padx=10, pady=10)

        self.label_nota = tk.Label(self, text = "Calificacion:")
        self.label_nota.config(fg="#FFFFFF", background="#292929", font= ("Arial",12," bold"))
        self.label_nota.grid(row=2, column=0, padx=10, pady=10)

        #---- Entrada de texto -----
        
        # ENTRADA NOMBRE
        self.el_estudiante = tk.StringVar()
        self.entry_estudiante = tk.Entry(self, textvariable= self.el_estudiante)
        self.entry_estudiante.config(
            width=50,
            font= ("Arial",12)
            )
                    
        self.entry_estudiante.grid(
            row=0,
            column=1,
            padx=10,
            pady=10,
            columnspan=2
            )

        # ENTRADA ASIGNATURA 
        self.la_asignatura = tk.StringVar()
        self.entry_asignatura = tk.Entry(self, textvariable= self.la_asignatura)
        self.entry_asignatura.config(
            width=50,
            font= ("Arial",12)
            )
        
        self.entry_asignatura.grid(
            row=1,
            column=1,
            padx=10,
            pady=10,
            columnspan=2
            )
        
        # ENTRADA NOTA
        self.la_nota = tk.StringVar()
        self.entry_nota = tk.Entry(self, textvariable= self.la_nota)
        self.entry_nota.config(
            width=50,
            font= ("Arial",12)  
            )
        
        self.entry_nota.grid(
            row=2,
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
            row=3,
            column=0,
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
            row=3,
            column=1,
            padx=10,
            pady=10,
        )

        #BOTON DE ELIMINAR
        self.boton_eliminar = tk.Button(self, text="Eliminar")
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
            column=2,
            padx=10,
            pady=10,
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
            row=5,
            column=2,
            padx=10,
            pady=10,
        )

        #BOTON DE SALIR
        self.boton_salir = tk.Button(self, text="Salir", command=self.deshabilitar_campos)
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
            row=5,
            column=0,
            padx=10,
            pady=10,
        )

    def habilitar_campos(self):
        self.el_estudiante.set("")
        self.la_asignatura.set("")
        self.la_nota.set("")

        self.entry_estudiante.config(state="normal")
        self.entry_asignatura.config(state="normal")
        self.entry_nota.config(state="normal")

        self.boton_guardar.config(state="normal")
        self.boton_eliminar.config(state="normal")

    def deshabilitar_campos(self):
        self.el_estudiante.set("")
        self.la_asignatura.set("")
        self.la_nota.set("")

        self.entry_estudiante.config(state="disabled")
        self.entry_asignatura.config(state="disabled")
        self.entry_nota.config(state="disabled")

        self.boton_guardar.config(state="disabled")
        self.boton_eliminar.config(state="disabled")
    
    def guardar_datos(self):

        pygrades = Pygrades(
            self.el_estudiante.get(),
            self.la_asignatura.get(),
            self.la_nota.get(),
        )

        guardar(pygrades)
        self.view()

        self.deshabilitar_campos()

    def view (self):
        self.lista_pygrade = listar()
        self.lista_pygrade.reverse()
        self.tabla = ttk.Treeview(self, columns= ("Estudiante", "Asignatura", "Calificacion"))

        self.tabla.grid(
            row=4,
            column=0, columnspan=4,
            sticky="nse"
        )

       #BARRA DE DESPLAZAMIENTO DE LA LISTA
        self.scroll = ttk.Scrollbar(self, orient= "vertical", command=self.tabla.yview)

        self.scroll.grid(
            row=4,
            column=4,
            sticky="nse"
        )

        self.tabla.heading("#0", text="Estudiante")
        self.tabla.heading("#1", text="Asignatura")
        self.tabla.heading("#2", text="Calificacion")

        for p in self.lista_pygrade:

            self.tabla.insert('',0, text=p[0], 
            values=(p[1], p[2], p[3]))
