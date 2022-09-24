import sqlite3
import csv


def file_input():
    from menu_test import Menu
    file_path = input("Please enter the file path: ")
    if file_path == 'b':
        print("Returning to main menu")
        Menu().menu_loop()
    return file_path

def conn_to_db(filename):
    return sqlite3.connect(filename)
    

def cursor(connection):   
    cursor = connection.cursor()
    return cursor


def import_csv_file():  
    while True:
        try:
            with open(file_input(), 'r', encoding='UTF-8', newline='') as fin:
                dict_reader = csv.DictReader(fin)
                persons = [(i['Firstname'], i['Lastname'], i["Birthdate"], i["Address"], i['Fullname']) for i in dict_reader]
                return persons
        except FileNotFoundError:
            print("Not a valid path, try again or 'b' to go back.")
        except PermissionError:
            print("Not a valid path, try again or 'b' to go back.")
            
def create_table(connection):
    connection.execute('CREATE TABLE IF NOT EXISTS persons (firstname, lastname, birthdate, address, fullname,  CONSTRAINT name_unique UNIQUE (firstname, lastname, address));')
    connection.commit()

           
def insert_to_db(connection): 
    connection.executemany('INSERT OR REPLACE INTO persons (firstname, lastname, birthdate, address, fullname) VALUES (?, ?, ?, ?, ?);', import_csv_file())
    connection.commit()
    print("Update to database successful")


def close_connection(connection):
    if connection:
        connection.close()
        print('SQLite Connection closed')

     
def main():
    with conn_to_db('db\SQLiteDB.db') as conn:
        print("Connection to SQL open.")
        cursor(conn)
        create_table(conn)