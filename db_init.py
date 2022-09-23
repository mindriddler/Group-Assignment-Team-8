import sqlite3
import csv


# Path to csv file. Important to write it as C:\Users\Fredrik\Desktop\Repos\Nackademin\Programmering_Systemering\GroupAssignmentDevOps22\data\persons.csv" 
# Otherwise it might not work. You will need to specify your path to your copy of the file ofcourse
def file_input():
    while True:
        try:
            file_path = input("Please enter the file path: ") 
            return file_path
        except ValueError:
            print("Not a valid input, try again")

def conn_to_db(filename):
    return sqlite3.connect(filename)
    

def cursor(connection):   
    cursor = connection.cursor()
    return cursor


def import_csv_file():  
    # Import csv and extract data, this is where we need to start. 
    # Basicly open up the CSV file and importing the raw text into the DB
    while True:
        try:
            with open(file_input(), 'r', encoding='UTF-8', newline='') as fin:
                dict_reader = csv.DictReader(fin)
                persons = [(i['id'], i['Firstname'], i['Lastname'], i["Birthdate"], i["Address"]) for i in dict_reader]
                return persons
        except FileNotFoundError:
            print("Not a valid path, try again")
        except PermissionError:
            print("Not a valid path, try again")
            
def create_table(connection):
    # Remove comment to create table, but after the table is created, comment this line back
    # This is where we create the table.
    connection.execute('CREATE TABLE IF NOT EXISTS persons (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, firstname, lastname, birthdate, address, CONSTRAINT name_unique UNIQUE (firstname, lastname, address));')
    connection.commit()
            
def insert_to_db(connection): 
    # Remove comment to insert data, but after the data is inserted, comment this line back 
    # And this is where the data from the persons.csv file get imported
    connection.executemany('INSERT OR IGNORE INTO persons (id, firstname, lastname, birthdate, address) VALUES (?, ?, ?, ?, ?);', import_csv_file())
    connection.commit()


# Code not in use as for now, removing at a later date if its not needed again           
"""def execute_select(cursor):
    # Show the table
    result = cursor.execute('SELECT * FROM persons')
    return result

def print_fetch_all(result): 
     # View result. Remove comment to print data from the DB
    for all in result:
        print(all)"""

def close_connection(connection):
    if connection:
        connection.close()
        print('SQLite Connection closed')

     
def main():
    with conn_to_db('db\SQLiteDB.db') as conn:
        print("Connection to SQL open.")
        cursor(conn)
        create_table(conn)
        insert_to_db(conn)
    
    

