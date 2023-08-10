import sqlite3
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
class Students:
    def __init__(self, Nombre, Asignatura, Calificacion ):
        self.Nombre = Nombre
        self.Asignatura = Asignatura
        self.Calificacion = Calificacion

    def __str__(self):
        return f"Students[{self.Nombre}, {self.Asignatura}, {self.Calificacion}]"
    
#---------------------------------------- FUNCIONES -------------------------------------------

#----- CREAR TABLA ------------
def crear_tabla():
    conexion = ConexionDB()

    sql_estd = '''
        CREATE TABLE students(
            StudentID INTEGER,
            is_teacher INTEGER,
            Nombre VARCHAR(50),
            Usuario VARCHAR(30),
            Contraseña VARCHAR(30),
            Asignatura VARCHAR(50),
            Calificación INTEGER,
            PRIMARY KEY (StudentID AUTOINCREMENT)
        )'''

    sql_prof = '''
        CREATE TABLE teachers(
            TeacherID INTEGER,
            is_teacher INTEGER,
            Nombre VARCHAR(50),
            Usuario VARCHAR(30),
            Contraseña VARCHAR(30),
            PRIMARY KEY (TeacherID AUTOINCREMENT)
        )'''
    
    conexion.cursor.execute(sql_estd)
    conexion.cursor.execute(sql_prof)

    titulo = "Crear Base de Datos"
    mensaje = "La base datos ha sido creada con exito"
    messagebox.showinfo(titulo,mensaje)

#----- BORRAR TABLA -----------
def borrar_tabla():
    conexion = ConexionDB()

    sql_estd = 'DROP TABLE students'
    sql_prof = 'DROP TABLE teachers'

    conexion.cursor.execute(sql_estd)
    conexion.cursor.execute(sql_prof)
    conexion.cerrar()

    titulo = "Borrar registro"
    mensaje = "Las tablas han sido borradas con exito"
    messagebox.showinfo(titulo,mensaje)


    #try:
     #   conexion.cursor.execute(sql_user)
     #   conexion.cursor.execute(sql_estd)
       # conexion.cursor.execute(sql_asign)
      #  conexion.cursor.execute(sql_calif)
       # conexion.cursor.execute(sql_prof)
       # conexion.cerrar()
       # titulo = "Borrar registro"
       # mensaje = "Las tablas han sido borradas con exito"
       # messagebox.showinfo(titulo,mensaje)
    #except:
       # titulo = "Borrar registro"
       # mensaje = "No hay tablas para borrar"
       # messagebox.showerror(titulo,mensaje)
    
#---- GUARDAR REGISTRO --------    
def guardar(Students):
    conexion = ConexionDB()

    sql_estd = f"""INSERT INTO students (Nombre, Asignatura, Calificación)
            VALUES('{Students.Nombre}', '{Students.Asignatura}', '{Students.Calificacion}')"""

    try:
        conexion.cursor.execute(sql_estd)
        conexion.cerrar()

        titulo = 'Conexion al Registro'
        mensaje = 'Se ha añadido el nuevo registro'
        messagebox.showinfo(titulo, mensaje)

    except:
        titulo = 'Conexion al Registro'
        mensaje = 'La tabla pygrades no esta creada en la base de datos'
        messagebox.showerror(titulo, mensaje)

#-- LISTAR TODOS LOS REGISTROS ---
def listar():
    conexion = ConexionDB()
    
    lista_students = []
    sql_estd = 'SELECT * FROM students'

    try:
        conexion.cursor.execute(sql_estd)       

        lista_students = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = 'Conexion al Registro' 
        mensaje = 'Crea la tabla en la base de datos'
        messagebox.showerror(titulo, mensaje)

    return lista_students

#---- EDITAR REGISTRO ---------
def editar(Students, id_student):
    conexion = ConexionDB()
    
    sql = f"""
        UPDATE students
        SET Nombre ='{Students.Nombre}',
        Asignatura ='{Students.Asignatura}',
        Calificación ='{Students.Calificacion}'
        WHERE StudentID={id_student}"""
    
    conexion.cursor.execute(sql)
    conexion.cerrar()

#---- ELIMINAR REGISTRO ---------
def eliminar(id_student):
    conexion = ConexionDB()
    
    sql = f'DELETE FROM students WHERE StudentID = {id_student}'
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()

        titulo = "Eliminar Datos"
        menseje = "Se ha eliminado el registro"
        messagebox.showinfo(titulo,menseje)
    except:
        titulo = "Eliminar Datos"
        menseje = "No se pudo eliminar este registro"
        messagebox.showerror(titulo,menseje)


def listar_estd(student_name:str):
    conexion = ConexionDB()
    lista_student = []
    sql = f"""SELECT * FROM students WHERE Nombre = '{student_name}'"""

    try:
        conexion.cursor.execute(sql)
        lista_student = conexion.cursor.fetchall()
        conexion.cerrar()

        if not lista_student:
            titulo = 'Estudiante no encontrado'
            mensaje = 'No se encontró el estudiante en la base de datos.'
            messagebox.showerror(titulo, mensaje)
    except sqlite3.Error:
        titulo = 'Error de conexión'
        mensaje = 'Ocurrió un error al conectar con la base de datos.'
        messagebox.showerror(titulo, mensaje)

    return lista_student