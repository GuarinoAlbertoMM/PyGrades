import sqlite3

username:str = 'Guarino Mendoza'
password:str = 'GuarinoMendoza1'

#This function enters the data base and gets all the important data of the user
def get_user_data(username:str,password:str):
    userName = []
    userPassword = []
    rol = []

    # Connect to the database
    conn = sqlite3.connect('database/pygradesDB.db')

    # Create a cursor object
    cursor = conn.cursor()

    # Execute the SELECT statement to enter the grade table
    cursor.execute("SELECT * FROM administrador")
    #cursor.execute("SELECT * FROM teachers")

    # Fetch all the rows
    rows = cursor.fetchall()

    # Print the grades
    for row in rows:
        if(username == row[3] and password == row[4]):
            userName.append(row[3])
            userPassword.append(row[4])
            rol.append(row[5])
            
    cursor.execute("SELECT * FROM profesor")

    # Fetch all the rows
    rows = cursor.fetchall()

    # Print the grades
    for row in rows:
        if(username == row[4] and password == row[5]):
            userName.append(row[4])
            userPassword.append(row[5])
            rol.append(row[6])
            
    cursor.execute("SELECT * FROM estudiante")

    # Fetch all the rows
    rows = cursor.fetchall()

    # Print the grades
    for row in rows:
        if(username == row[5] and password == row[6]):
            userName.append(row[5])
            userPassword.append(row[6])
            rol.append(row[7])
            

    conn.close()

    print("Usuario:", userName)
    print("Contra:", userPassword)
    print("Rol:", rol)     

    #Return all the data that is necessary
    return userName, userPassword, rol

get_user_data(username,password)