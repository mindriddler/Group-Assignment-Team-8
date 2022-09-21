import sqlite3
import csv



# Path to csv file. Important to write it as C:\Users\Fredrik\Desktop\Repos\Nackademin\Programmering_Systemering\GroupAssignmentDevOps22\data\persons.csv" 
# Otherwise it might not work. You will need to specify your path to your copy of the file ofcourse

file_path = input("Please enter the file path: ") 
db_path = input("Please enter the path to the DB: ")
# C:\Users\Fredrik\Desktop\Repos\Nackademin\Programmering_Systemering\GroupAssignmentDevOps22\data\persons.csv

try:
  
    # Import csv and extract data, this is where we need to start. 
    # Basicly open up the CSV file and importing the raw text into the DB
    with open(file_path, 'r') as fin:
        dict_reader = csv.DictReader(fin)
        persons = [(i['Index'], i['Firstname'], i['Lastname'], i["Birthdate"], i["Address"]) for i in dict_reader]
        # print(persons)
  
    # Connect to SQLite. 
    # This creates the connection to the database, which is needed to make changes to it. Its not the same as writing a textfile or w/e
    sqliteConnection = sqlite3.connect(db_path)
    cursor = sqliteConnection.cursor()
  
    # Remove comment to create table, but after the table is created, comment this line back
    # This is where we create the table.
    cursor.execute('create table persons (`index`, firstname, lastname, birthdate, address);')
  
    # Remove comment to insert data, but after the data is inserted, comment this line back 
    # And this is where the data from the persons.csv file get imported
    cursor.executemany("insert into persons (`index`, firstname, lastname, birthdate, address) VALUES (?, ?, ?, ?, ?);", persons)
  
    # Show the table
    cursor.execute('select * from persons;')
  
    # View result. Remove comment to print data from the DB
    result = cursor.fetchall()
    print(result)
  
    # Commit work and close connection. 
    # Think Git :') 
    # We need to commit our changes to the database for it in order for it to get updated with the new information
    # If we want to make sure that our changes get commited to the database,
    # we can just add sqliteConnection.commit() after each execute command that changes stuff
    
    sqliteConnection.commit() 
    cursor.close()
    
# except sqlite3.Error as error:
        # print('Error occured - ', error)
except FileNotFoundError as error2:
    print("Wrong path specified -", error2)
 
# I didnt like it when the console was filled with error text so i made a few more try/except to intercept all of the possible errors
# try:
    # if sqliteConnection:
        # sqliteConnection.close()
        # print('SQLite Connection closed')
# except NameError as error3:
    # print("Wrong path specified -", error3)
    