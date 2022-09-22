import csv
import sys
import sqlite3
from db_init import conn_to_db, cursor, close_connection
from _classes import getlimitedRows
from _functions import update_db


class App:
    def __init__(self):
        pass

    # def conn_to_db(filename):
    #     return sqlite3.connect(filename)
    #     # with open(r'C:\\users\Fredrik\desktop\Repos\Nackademin\Programmering_Systemering\GroupAssignmentDevOps22\data\persons.csv') as f:
    #         # reader = csv.reader(f)
    #         # for row in reader:
    #             # print(row)

    def delete_a_person(self):                                                                                                               ## Delete OK?
        choice2 = input("Who do you want to delete?: ")
        
        try:
            # del self.name
            conn = sqlite3.connect('db\SQLiteDB.db')
            cursor = conn.cursor()
            # delete_user = str(input("Who do you want to delete?: "))
            delete_query = ("DELETE from persons WHERE `firstname` = ?")
            cursor.execute(delete_query, (choice2,))
            conn.commit()
            print("Entry Deleted")
            cursor.close()
        except AttributeError:
                print("No object to delete")

    def update_a_persons_address(self):
        print(f"# EXTRA EXTRA")

    def quit(self):
        print('Shutting down')
        self.run = False
        sys.exit(0)

class Menu:

    MAIN_MENU_TEXT = """
'-------------------------'
'------- Main Menu -------'
'-------------------------'                                     
1: 'List all persons'                                            #EXTRA (a, b, c, d)
2: 'Delete a person'
3: 'Update a persons address'                                    #EXTRA EXTRA
4: 'Quit'
"""

    def __init__(self) -> None:
        pass

    def user_input(self):
        return int(input("Enter your choice [1-4]: "))

    def menu_choice(self, choice):
        if choice == 4:
            self.running = False
        elif choice == 1:
            getlimitedRowssize = int(input("How many rows to you want to show?: "))
            getlimitedRows(conn_to_db('db\SQLiteDB.db'), getlimitedRowssize)
        elif choice == 2:
            App().delete_a_person()
        elif choice == 3:
            update_db()

    def menu_loop(self):
        self.running = True
        while self.running:
            print(Menu.MAIN_MENU_TEXT)
            choice = self.user_input()
            self.menu_choice(choice)


def main2():
    with conn_to_db('db\SQLiteDB.db') as conn:
        cursor(conn)
        Menu().menu_loop()
    close_connection(conn)




if __name__ == '__main__':
    main2()
    