import sqlite3

username:str = 'Guarino Mendoza'
password:str = 'GuarinoMendoza'

#This function enters the data base and gets all the important data of the user
def get_user_data(username:str,password:str):
    userName = []
    userPassword = []
    userId = []
    isTeacher = []

    # Connect to the database
    conn = sqlite3.connect('pygrades.db')

    # Create a cursor object
    cursor = conn.cursor()

    # Execute the SELECT statement to enter the grade table
    cursor.execute("SELECT * FROM user")

    # Fetch all the rows
    rows = cursor.fetchall()

    # Print the grades
    for row in rows:
        if(username == row[1] and password == row[2]):
            userName.append(row[1])
            userPassword.append(row[2])
            userId.append(row[0])
            if(row[3]==1):
                isTeacher.append(row[3])
            else:
                isTeacher = [0]

    conn.close()

    print("Usuario:", userName)
    print("Contra:", userPassword)     

    #Return all the data that is necessary
    return userName, userPassword, userId, isTeacher

get_user_data(username, password)