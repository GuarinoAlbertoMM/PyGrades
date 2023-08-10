import sqlite3

username:str = 'Guarino Mendoza'
password:str = 'GuarinoMendoza1'

#This function enters the data base and gets all the important data of the user
def get_user_data(username:str,password:str):
    userName = []
    userPassword = []
    isTeacher = []
    user_name = []

    # Connect to the database
    conn = sqlite3.connect('database/pygradesDB.db')

    # Create a cursor object
    cursor = conn.cursor()

    # Execute the SELECT statement to enter the grade table
    cursor.execute("SELECT * FROM students")
    #cursor.execute("SELECT * FROM teachers")

    # Fetch all the rows
    rows = cursor.fetchall()

    # Print the grades
    for row in rows:
        if(username == row[3] and password == row[4]):
            userName.append(row[3])
            userPassword.append(row[4])
            isTeacher.append(row[1])
            user_name.append(row[2])
            
    cursor.execute("SELECT * FROM teachers")

    # Fetch all the rows
    rows = cursor.fetchall()

    # Print the grades
    for row in rows:
        if(username == row[3] and password == row[4]):
            userName.append(row[3])
            userPassword.append(row[4])
            isTeacher.append(row[1])
            user_name.append(row[2])
            

    conn.close()

    print("Usuario:", userName)
    print("Contra:", userPassword)
    print("Es profe?:", isTeacher)
    print("Nombre:", user_name )      

    #Return all the data that is necessary
    return userName, userPassword, isTeacher, user_name

get_user_data(username,password)