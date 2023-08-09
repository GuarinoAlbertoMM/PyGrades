from .conexion_db import ConexionDB
from tkinter import messagebox

#----------------------------------------- CLASES -------------------------------------------

#----- TABLA ADMIN --------
class Administrador:
    def __init__(self, Nombre_admn, Apellido_admn, Usuario_admn, Contraseña_admn):
        self.ID_admin = None
        self.Nombre_admn =  Nombre_admn
        self.Apellido_admn = Apellido_admn
        self.Usuario_admn = Usuario_admn
        self.Contraseña_admn = Contraseña_admn

    def __str__(self):
        return f'Administrador[{self.Nombre_admn}, {self.Apellido_admn}, {self.Usuario_admn}, {self.Contraseña_admn}]'

#---- TABLA PROFESORES -----
class Profesor:
    def __init__(self,Nombre_pfsr, Apellido_pfsr, Asignatura_pfsr, Usuario_pfsr, Contraseña_pfsr):
        self.ID_Profesor = None
        self.Nombre_pfsr = Nombre_pfsr
        self.Apellido_pfsr = Apellido_pfsr
        self.Asignatura_pfsr = Asignatura_pfsr
        self.Usuario_pfsr = Usuario_pfsr
        self.Contraseña_pfsr = Contraseña_pfsr

    def __str__(self):
        return f"profesor[{self.Nombre_pfsr}, {self.Apellido_pfsr}, {self.Asignatura_pfsr}, {self.Usuario_pfsr}, {self.Contraseña_pfsr}]"

#---- TABLA ESTUDIANTE -----
class Estudiante:
    def __init__(self,Nombre_etdt,Apellido_etdt,Edad_etdt,Usuario_etdt,Contraseña_etdt):
        self.ID_Estudiante = None
        self.Nombre_etdt = Nombre_etdt
        self.Apellido_etdt = Apellido_etdt
        self.Edad_etdt = Edad_etdt 
        self.Usuario_etdt = Usuario_etdt
        self.Contraseña_etdt = Contraseña_etdt

    def __str__(self):
        return f"estudiante[{self.Nombre}, {self.Apellido}, {self.Edad}, {self.Est_Usuario}, {self.Contraseña}]"
    
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
        PRIMARY KEY(ID_admin AUTOINCREMENT)
    )'''
    

    sql2 = '''
    CREATE TABLE profesor(
        ID_Profesor INTEGER,
        Nombre_pfsr VARCHAR(30),
        Apellido_pfsr VARCHAR(30),
        Asignatura_pfsr VARCHAR(30),
        Usuario_pfsr VARCHAR(20),
        Contraseña_pfsr VARCHAR(10),
        PRIMARY KEY(ID_Profesor AUTOINCREMENT)
    )'''
    
    sql3 = '''
    CREATE TABLE estudiante(
        ID_Estudiante INTEGER,
        Nombre_etdt VARCHAR(50),
        Apellido_etdt VARCHAR(50),
        Edad_etdt INTEGER,
        Usuario_etdt VARCHAR(20),
        Contraseña_etdt VARCHAR(10),
        PRIMARY KEY(ID_Estudiante AUTOINCREMENT)
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

    sql1 = 'DROP TABLE administrador'
    sql2 = 'DROP TABLE profesor'
    sql3 = 'DROP TABLE estudiante'

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
def guardar_ADMN(administrador):
    conexion = ConexionDB()

    sql1 = f"""INSERT INTO administrador (Nombre_admn, Apellido_admn, Usuario_admn, Contraseña_admn)
            VALUES('{administrador.Nombre_admn}', '{administrador.Apellido_admn}', '{administrador.Usuario_admn}', '{administrador.Contraseña_admn}')"""


    try:
        conexion.cursor.execute(sql1)
        conexion.cerrar()

    except:
        titulo = 'Conexion al Registro'
        mensaje = 'La tabla pygrades no esta creada en la base de datos'
        messagebox.showerror(titulo, mensaje)

def guardar_PFSR(profesor):
    conexion = ConexionDB()

    sql2 = f"""INSERT INTO profesor (Nombre_pfsr, Apellido_pfsr, Asignatura_pfsr, Usuario_pfsr, Contraseña_pfsr)
            VALUES('{profesor.Nombre_pfsr}', '{profesor.Apellido_pfsr}', '{profesor.Asignatura_pfsr}', '{profesor.Usuario_pfsr}', '{profesor.Contraseña_pfsr}')"""

    try:
        conexion.cursor.execute(sql2)
        conexion.cerrar()

    except:
        titulo = 'Conexion al Registro'
        mensaje = 'La tabla pygrades no esta creada en la base de datos'
        messagebox.showerror(titulo, mensaje)

def guardar_ETDT(estudiante):
    conexion = ConexionDB()

    sql3 = f"""INSERT INTO estudiante (Nombre_etdt, Apellido_etdt, Edad_etdt, Usuario_etdt, Contraseña_etdt)
            VALUES('{estudiante.Nombre_etdt}', '{estudiante.Apellido_etdt}', '{estudiante.Edad_etdt}', '{estudiante.Usuario_etdt}', '{estudiante.Contraseña_etdt}')"""

    try:
        conexion.cursor.execute(sql3)
        conexion.cerrar()

    except:
        titulo = 'Conexion al Registro'
        mensaje = 'La tabla pygrades no esta creada en la base de datos'
        messagebox.showerror(titulo, mensaje)
#-- SELECCIONAR PARA EDITAR ---
#def listar():
    #conexion = ConexionDB()
    
    #lista_administrador = []
    #sql1 = 'SELECT * FROM administrador'

    #lista_profesor = []
    #sql2 = 'SELECT * FROM profesor'

    #lista_estudiante = []
    #sql3 = 'SELECT * FROM estudiante'

    #try:
     #   conexion.cursor.execute(sql1)
      #  conexion.cursor.execute(sql2)
       # conexion.cursor.execute(sql3)        

  #      lista_administrador = conexion.cursor.fetchall()
   #     lista_profesor = conexion.cursor.fetchall()
    #    lista_estudiante = conexion.cursor.fetchall()
     #   conexion.cerrar()
    #except:
     #   titulo = 'Conexion al Registro' 
      #  mensaje = 'Crea la tabla en la base de dato'
       # messagebox.showerror(titulo, mensaje)

#    return lista_administrador, lista_profesor, lista_estudiante

#---- EDITAR REGISTRO ---------
#def editar (administrador, ID_admin, Profesor, Prf_Usuario, Estudiantes, Est_Usuario):
 #   conexion = ConexionDB()

  #  sql1 = f""" UPDATE administrador
   # SET administrador = '{administrador.Estudiante}', Asignatura = '{administrador.Asignatura}', Calificacion = '{administrador.Calificacion}'
    #WHERE ID_Estudiante = {ID_admin}""" 
    
#    sql2 = f""" UPDATE Profesores
 #   SET Estudiante = '{Profesor.Estudiante}', Asignatura = '{administrador.Asignatura}', Calificacion = '{administrador.Calificacion}'
  #  WHERE ID_Estudiante = {ID_Profesor}""" 

   # sql3 = f""" UPDATE Estudiantes
#    SET Estudiante = '{administrador.Estudiante}', Asignatura = '{administrador.Asignatura}', Calificacion = '{administrador.Calificacion}'
 #   WHERE ID_Estudiante = {ID_Estudiante}""" 

  #  try:
   #     conexion.cursor.execute(sql)
    #    conexion.cerrar()
 #   except:
  #      titulo = "Edición de datos"
   #     menseje = "No se pudo editar este registro"
    #    messagebox.showerror(titulo,menseje)

#def eliminar(ID_Estudiante):
#    conexion = ConexionDB()
    
 #   sql = f'DELETE FROM pygrades WHERE ID_Estudiante = {ID_Estudiante}'
    
  #  try:
   #     conexion.cursor.execute(sql)
    #    conexion.cerrar()
    #except:
     #   titulo = "Eliminar Datos"
      #  menseje = "No se pudo eliminar este registro"
       # messagebox.showerror(titulo,menseje)

        


