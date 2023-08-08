from .conexion_db import ConexionDB
from tkinter import messagebox
#CREAR DATOS - INSERTAR DATOS

def crear_tabla():
    conexion = ConexionDB()

    sql = '''
    CREATE TABLE pygrades(
        ID_Estudiante INTEGER,
        Estudiante VARCHAR(50),
        Asignatura VARCHAR(50),
        Calificacion INTEGER,
        PRIMARY KEY(id_estudiante AUTOINCREMENT)
        )'''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = "Crear_registro"
        mensaje = "Se creo la tabla en la base de dato"
        messagebox.showinfo(titulo,mensaje)
    except:
        titulo = "Crear_registro"
        mensaje = "La base de datos ya está creada"
        messagebox.showwarning(titulo,mensaje)

def borrar_tabla():
    conexion = ConexionDB()

    sql = 'DROP TABLE pygrades'

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = "Borrar_registro"
        mensaje = "La tabla ha sido borrada con exito"
        messagebox.showinfo(titulo,mensaje)
    except:
        titulo = "Borrar_registro"
        mensaje = "No hay tabla para borrar"
        messagebox.showerror(titulo,mensaje)

class Pygrades:
    def __init__(self, Estudiante, Asignatura, Calificacion):
        self.ID_Estudiante = None
        self.Estudiante =  Estudiante
        self.Asignatura = Asignatura
        self.Calificacion = Calificacion
    
    def __str__(self):
        return f"Pygrades[{self.Estudiante}, {self.Asignatura}, {self.Calificacion}]"
    
def guardar(pygrades):
    conexion =ConexionDB()

    sql = f"""INSERT INTO pygrades (Estudiante, Asignatura, Calificacion)
    VALUES('{pygrades.Estudiante}', '{pygrades.Asignatura}', '{pygrades.Calificacion}')"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()

    except:
        titulo = 'Conexion al Registro'
        mensaje = 'La tabla pygrades no esta creada en la base de datos'
        messagebox.showerror(titulo, mensaje)

def listar():
    conexion = ConexionDB()
    
    lista_pygrades = []
    sql = 'SELECT * FROM pygrades'

    try:
        conexion.cursor.execute(sql)
        lista_pygrades = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = 'Conexion al Registro'
        mensaje = 'Crea la tabla en la base de dato'
        messagebox.showerror(titulo, mensaje)

    return lista_pygrades

    