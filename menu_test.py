import sys
from _classes import clazz
from update_address import update_db, delete_a_person
from db_init import close_connection, conn_to_db

class Menu:

    MAIN_MENU_TEXT = """
'-------------------------'
'------- Main Menu -------'
'-------------------------'                                     
1: 'List all persons'                   # Base function is working, next task work on #EXTRA (a, b, c, d)
2: 'Delete a person'                    # Works as intended
3: 'Update a persons address'           # Works as intended
4: 'Quit'                               # Works as intended
"""




    def __init__(self):
        pass

    def user_input(self):
        return int(input("Enter your choice [1-4]: "))

    def menu_choice(self, choice):
        if choice == 4:
            self.running = False
            close_connection(conn_to_db('db\SQLiteDB.db'))
            print("Exiting the program. Have a nice day.")
        elif choice == 1:
            clazz()
        elif choice == 2:
            delete_a_person()
        elif choice == 3:
            update_db()

    def menu_loop(self):
        self.running = True
        while self.running:
            print(Menu.MAIN_MENU_TEXT)
            choice = self.user_input()
            self.menu_choice(choice)
            
def menu_main():
    Menu().menu_loop()