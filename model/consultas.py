from .conexion_db import ConexionDB
from tkinter import messagebox

#----------------------------------------- CLASES -------------------------------------------

#----- TABLA ADMIN --------
class Pygrades:
    def __init__(self, Estudiante, Asignatura, Calificacion):
        self.ID_Estudiante = None
        self.Estudiante =  Estudiante
        self.Asignatura = Asignatura
        self.Calificacion = Calificacion

    def __str__(self):
        return f"Pygrades[{self.Estudiante}, {self.Asignatura}, {self.Calificacion}]"

#---- TABLA PROFESORES -----
class Profesores:
    def __init__(self,Nombre, Apellido, Asignatura, Prf_Usuario, Contraseña,):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Asignatura = Asignatura
        self.Prf_Usuario = Prf_Usuario
        self.Contraseña = Contraseña

    def __str__(self):
        return f"Profesores[{self.Nombre}, {self.Apellido}, {self.Asignatura}, {self.Prf_Usuario}, {self.Contraseña}]"

#---- TABLA ESTUDIANTE -----
class Estudiantes:
    def __init__(self,Nombre, Apellido, Edad, Est_Usuario, Contraseña,):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Edad = Edad
        self.Est_Usuario = Est_Usuario
        self.Contraseña = Contraseña

    def __str__(self):
        return f"Profesores[{self.Nombre}, {self.Apellido}, {self.Edad}, {self.Est_Usuario}, {self.Contraseña}]"
    
#---------------------------------------- FUNCIONES -------------------------------------------

#----- CREAR TABLA ------------
def crear_tabla():
    conexion = ConexionDB()

    sql1 = '''
    CREATE TABLE administrador(
        ID_admin INTEGER,
        Nombre_admn VARCHAR(30),
        Apellido_admn VARCHAR(30),
        Usuario_admn VARCHAR(30),
        Contraseña_admn VARCHAR(30),
        (ID_Profesor AUTOINCREMENT),
        PRIMARY KEY (Usuario)
        )'''
    

    sql2 = '''
    CREATE TABLE profesor(
        ID_Profesor INTEGER AUTOINCREMENT,
        Nombre VARCHAR(30),
        Apellido VARCHAR(30),
        Asignatura VARCHAR(30),
        Usuario_pfsr VARCHAR(20),
        Contraseña VARCHAR(10),
        PRIMARY KEY(Usuario)
    )'''
    
    sql3 = '''
    CREATE TABLE estudiante(
        ID_Estudiante INTEGER AUTOINCREMENT,
        Nombre VARCHAR(50),
        Apellido VARCHAR(50),
        Edad INTEGER,
        Usuario_etdt VARCHAR(20),
        Contraseña VARCHAR(10),
        PRIMARY KEY(Usuario)

    )'''

    try:
        conexion.cursor.execute(sql1)
        conexion.cursor.execute(sql2)
        conexion.cursor.execute(sql3)
        
        conexion.cerrar()
        titulo = "Crear Base Datos"
        mensaje = "La base datos ha sido creada con exito"
        messagebox.showinfo(titulo,mensaje)
    except:
        titulo = "Crear Base Datos"
        mensaje = "No hay base datos para crear"
        messagebox.showerror(titulo,mensaje)

#----- BORRAR TABLA -----------
def borrar_tabla():
    conexion = ConexionDB()

    sql1 = 'DROP TABLE aministrador'
    sql2 = 'DROP TABLE profesor'
    sql3 = 'DROP TABLE estudiante'
    sql4 = 'DROP TABLE sqlite_sequence'

    try:
        conexion.cursor.execute(sql1)
        conexion.cursor.execute(sql2)
        conexion.cursor.execute(sql3)
        conexion.cerrar()
        titulo = "Borrar_registro"
        mensaje = "La tabla ha sido borrada con exito"
        messagebox.showinfo(titulo,mensaje)
    except:
        titulo = "Borrar_registro"
        mensaje = "No hay tabla para borrar"
        messagebox.showerror(titulo,mensaje)
    
#---- GUARDAR REGISTRO --------    
def guardar(administrador, profesores, estudiantes):
    conexion = ConexionDB()

    sql1 = f"""INSERT INTO administrador (Nombre_admn, Apellido_admn, Usuario_admn, Contraseña_admn)
            VALUES('{administrador.Nombre_admn}', '{administrador.Apellido_admn}', '{administrador.Usuario_admn}', '{administrador.Contraseña_admn}')"""

    sql2 = f"""INSERT INTO profesores (Nombre, Apellido, Asignatura, Usuario_pfsr, Contraseña)
            VALUES('{profesores.Nombre}', '{profesores.Apellido}', '{profesores.Asignatura}', '{profesores.Usuario}', '{profesores.Contraseña}')"""

    sql3 = f"""INSERT INTO estudiantes (Nombre, Apellido, Edad, Usuario_etdt, Contraseña)
            VALUES('{estudiantes.Nombre}', '{estudiantes.Apellido}', '{estudiantes.Edad}', '{estudiantes.Usuario}', '{estudiantes.Contraseña}')"""

    try:
        conexion.cursor.execute(sql1)
        conexion.cursor.execute(sql2)
        conexion.cursor.execute(sql3)
        conexion.cerrar()

    except:
        titulo = 'Conexion al Registro'
        mensaje = 'La tabla pygrades no esta creada en la base de datos'
        messagebox.showerror(titulo, mensaje)

#-- SELECCIONAR PARA EDITAR ---
def listar():
    conexion = ConexionDB()
    
    lista_administrador = []
    sql1 = 'SELECT * FROM administrador'

    lista_profesor = []
    sql2 = 'SELECT * FROM profesor'

    lista_estudiante = []
    sql3 = 'SELECT * FROM estudiante'

    try:
        conexion.cursor.execute(sql1)
        conexion.cursor.execute(sql2)
        conexion.cursor.execute(sql3)        

        lista_administrador = conexion.cursor.fetchall()
        lista_profesor = conexion.cursor.fetchall()
        lista_estudiante = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = 'Conexion al Registro' 
        mensaje = 'Crea la tabla en la base de dato'
        messagebox.showerror(titulo, mensaje)

    return lista_administrador, lista_profesor, lista_estudiante

#---- EDITAR REGISTRO ---------
def editar (administrador, ID_admin, Profesor, Prf_Usuario, Estudiantes, Est_Usuario):
    conexion = ConexionDB()

    sql1 = f""" UPDATE administrador
    SET Estudiante = '{administrador.Estudiante}', Asignatura = '{administrador.Asignatura}', Calificacion = '{administrador.Calificacion}'
    WHERE ID_Estudiante = {ID_Estudiante}""" 
    
    sql2 = f""" UPDATE Profesores
    SET Estudiante = '{Profesor.Estudiante}', Asignatura = '{administrador.Asignatura}', Calificacion = '{administrador.Calificacion}'
    WHERE ID_Estudiante = {ID_Estudiante}""" 

    sql3 = f""" UPDATE Estudiantes
    SET Estudiante = '{administrador.Estudiante}', Asignatura = '{administrador.Asignatura}', Calificacion = '{administrador.Calificacion}'
    WHERE ID_Estudiante = {ID_Estudiante}""" 

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = "Edición de datos"
        menseje = "No se pudo editar este registro"
        messagebox.showerror(titulo,menseje)

def eliminar(ID_Estudiante):
    conexion = ConexionDB()
    
    sql = f'DELETE FROM pygrades WHERE ID_Estudiante = {ID_Estudiante}'
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = "Eliminar Datos"
        menseje = "No se pudo eliminar este registro"
        messagebox.showerror(titulo,menseje)

        


