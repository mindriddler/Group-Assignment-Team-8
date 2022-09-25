import sqlite3
from _classes import Person, Car_owned
from _functions import update_db, delete_a_person, query_persons_with_, add_vehicles, list_all_vehicles, delete_vehicle, wait
from db_init import close_connection, conn_to_db, insert_to_db

class Menu:

    MAIN_MENU_TEXT = """
'-------------------------'
'------- Main Menu -------'
'-------------------------'
Select what table to work with

1: 'Persons'
2: 'Vehicles'
3: 'Load data from file'
---------------------------
9: 'Quit'
"""

    VEHICLES_MENU_TEXT = """
'-------------------------'
'----- Vehicles Menu -----'
'-------------------------'
1: 'List all entrys'
2: 'Search and find correlation between vehicle and person tables'
3: 'Input an entry to the database'
4: 'Delete an entry'
-----------------------------------
8: 'Return to main menu'
9: 'Quit'
"""

    PERSON_MENU_TEXT = """
'-------------------------'
'------ Persons Menu -----'
'-------------------------'
1: 'List all entrys'        
2: 'Search and list specific entry'
3: 'Update an entrys address'
4: 'Delete an entry'
-----------------------------------
8: 'Return to main menu'
9: 'Quit'                       
"""

    def user_input(self):
        try:
            return int(input("Enter your choice: "))
        except ValueError:
            print("Invaild input, returning to main menu")

    
    def main_menu_choice(self, choice):
        if choice == 9:
            self.running = False
            close_connection(conn_to_db('db\SQLiteDB.db'))
            print("Exiting the program. Have a nice day.")
        elif choice == 3:
            insert_to_db(sqlite3.connect('db\SQLiteDB.db'))
        elif choice == 1:
            print(self.PERSON_MENU_TEXT)
            choice_2 = self.user_input()
            self.person_list_menu(choice_2)
        elif choice == 2:
            print(self.VEHICLES_MENU_TEXT)
            choice_2 = self.user_input()
            self.vehicles_list_menu(choice_2)
    
    
    
    def vehicles_list_menu(self, choice_2):
        try:
            if choice_2 == 3:
                add_vehicles()
            elif choice_2 == 2:
                Car_owned.car_print()
                wait()
            elif choice_2 == 1: 
                list_all_vehicles()
                wait()
            elif choice_2 == 4: 
                delete_vehicle()
            elif choice_2 == 9:
                self.running = False
                close_connection(conn_to_db('db\SQLiteDB.db'))
                print("Exiting the program. Have a nice day.")
            elif choice_2 == 8:
                self.menu_loop()
        except sqlite3.OperationalError as error_notable:
            print("Something went wrong -", error_notable)
    
    def person_list_menu(self, choice_2):
        try:    
            if choice_2 == 1:
                Person.people_print()
                wait()
            elif choice_2 == 2:
                query_persons_with_()
                wait()
            elif choice_2 == 3:
                update_db()
            elif choice_2 == 4:
                delete_a_person()
            elif choice_2 == 8:
                self.menu_loop()
            elif choice_2 == 9:
                self.running = False
                close_connection(conn_to_db('db\SQLiteDB.db'))
                print("Exiting the program. Have a nice day.")
        except sqlite3.OperationalError as error_notable:
            print("Something went wrong -", error_notable)


    def menu_loop(self):
        self.running = True
        while self.running:
            print(Menu.MAIN_MENU_TEXT)
            choice = self.user_input()
            self.main_menu_choice(choice)

def menu_main():
    Menu().menu_loop()