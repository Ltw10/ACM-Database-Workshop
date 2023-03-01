import pyodbc


def connectToDB():

    # Trusted Connection to Named Instance
    print("Attempting to connect to the database")
    connection = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=LUKES-XPS-15;DATABASE=workshopdb;Trusted_Connection=yes;Encrypt=No')
    print("Database connected")
    return connection

def executeQuery(connection):

    print("Executing Query")
    cursor=connection.cursor()
    cursor.execute("SELECT * from dbo.participantData")

    print("Printing Query \n")
    records = cursor.fetchall()
    for row in records:
        print("Name: " + row[0] + " " + row[1])
        print("Grade: " + row[2])
        print("Favorite Animal: " + row[3])
        print("\n")

    print("Table Values Printed")

    cursor.close()


def addTableData(connection):
    print("Adding Table Data")
    cursor=connection.cursor()
    sql = "INSERT INTO dbo.participantData VALUES (?, ?, ?, ?)"
    participantData = [('Test', 'Man', 'Grade', 'Animal')]
    
    cursor.executemany(sql, participantData)
        
    print("Table Data Added")

    cursor.close()
    
    

def main():
    connection = connectToDB()
    addTableData(connection)
    executeQuery(connection)
    connection.close()

main()