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
    CREATE TABLE pygrades(
        ID_Estudiante INTEGER,
        Estudiante VARCHAR(50),
        Asignatura VARCHAR(50),
        Calificacion INTEGER,
        PRIMARY KEY(ID_Estudiante AUTOINCREMENT)
        )'''
    

    sql2 = '''
    CREATE TABLE profesores(
        Nombre VARCHAR(30),
        Apellido VARCHAR(30),
        Asignatura VARCHAR(30),
        Usuario VARCHAR(20),
        Contraseña VARCHAR(10),
        PRIMARY KEY(Usuario)
    )'''
    
    sql3 = '''
    CREATE TABLE estudiantes(
        Nombre VARCHAR(50),
        Apellido VARCHAR(50),
        Edad INTEGER,
        Usuario VARCHAR(20),
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

    sql1 = 'DROP TABLE pygrades'
    sql2 = 'DROP TABLE profesores'
    sql3 = 'DROP TABLE estudiantes'
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
def guardar(pygrades, profesores, estudiantes):
    conexion = ConexionDB()

    sql1 = f"""INSERT INTO pygrades (Estudiante, Asignatura, Calificacion)
            VALUES('{pygrades.Estudiante}', '{pygrades.Asignatura}', '{pygrades.Calificacion}')"""

    sql2 = f"""INSERT INTO profesores (Nombre, Apellido, Asignatura, Usuario, Contraseña)
            VALUES('{profesores.Nombre}', '{profesores.Apellido}', '{profesores.Asignatura}', '{profesores.Usuario}', '{profesores.Contraseña}')"""

    sql3 = f"""INSERT INTO estudiantes (Nombre, Apellido, Edad, Usuario, Contraseña)
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
    
    lista_pygrades = []
    sql1 = 'SELECT * FROM pygrades'

    lista_profesores = []
    sql2 = 'SELECT * FROM profesores'

    lista_estudiantes = []
    sql3 = 'SELECT * FROM estudiantes'

    try:
        conexion.cursor.execute(sql1)
        conexion.cursor.execute(sql2)
        conexion.cursor.execute(sql3)        

        lista_pygrades = conexion.cursor.fetchall()
        lista_profesores = conexion.cursor.fetchall()
        lista_estudiantes = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = 'Conexion al Registro' 
        mensaje = 'Crea la tabla en la base de dato'
        messagebox.showerror(titulo, mensaje)

    return lista_pygrades, lista_profesores, lista_estudiantes

#---- EDITAR REGISTRO ---------
def editar (Pygrades, ID_Estudiante, Profesores, Prf_Usuario, Estudiantes, Est_Usuario):
    conexion = ConexionDB()

    sql1 = f""" UPDATE Pygrades
    SET Estudiante = '{Pygrades.Estudiante}', Asignatura = '{Pygrades.Asignatura}', Calificacion = '{Pygrades.Calificacion}'
    WHERE ID_Estudiante = {ID_Estudiante}""" 
    
    sql2 = f""" UPDATE Profesores
    SET Estudiante = '{Pygrade.Estudiante}', Asignatura = '{Pygrades.Asignatura}', Calificacion = '{Pygrades.Calificacion}'
    WHERE ID_Estudiante = {ID_Estudiante}""" 

    sql3 = f""" UPDATE Estudiantes
    SET Estudiante = '{Pygrades.Estudiante}', Asignatura = '{Pygrades.Asignatura}', Calificacion = '{Pygrades.Calificacion}'
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

        


