from _classes import clazz
from _functions import update_db, delete_a_person, quary_persons_with_
from db_init import close_connection, conn_to_db

class Menu:

    MAIN_MENU_TEXT = """
'-------------------------'
'------- Main Menu -------'
'-------------------------'                                     
1: 'List or search persons'             # Base function is working, next task work on #EXTRA (a, b, c, d)
2: 'Delete a person'                    # Works as intended
3: 'Update a persons address'           # Works as intended
4: 'Quit'                               # Works as intended
"""
    LIST_MENU_TEXT = """
'-------------------------'
'------- Main Menu -------'
'-------------------------'                                     
1: 'List all entrys'                   
2: 'Search and list specific entry'                    
3: 'Return to main menu'                              
"""


    def __init__(self):
        pass

    def user_input(self):
        try:
            return int(input("Enter your choice: "))
        except ValueError:
            print("Invaild input, returning to main menu")

    def menu_choice(self, choice):
        if choice == 4:
            self.running = False
            close_connection(conn_to_db('db\SQLiteDB.db'))
            print("Exiting the program. Have a nice day.")
        elif choice == 1:
            print(Menu.LIST_MENU_TEXT)
            choice_2 = self.user_input()
            self.list_menu(choice_2)            
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

    def list_menu(self, choice_2):
        if choice_2 == 1:
            clazz()
        elif choice_2 == 2:
            quary_persons_with_()
        elif choice_2 == 3:
            self.menu_loop()






            
def menu_main():
    Menu().menu_loop()