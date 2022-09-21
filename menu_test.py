import csv
import sys
import sqlite3
from _classes import Person
from _classes import clazz

class Greetings:
    def __init__(self, name):
        self.name = name

    def list_all_persons(self):
        clazz() # I have now made it so instead of writing the code here again, we are now instead
                # calling for this function which will get us all the entrys in the database printed to the terminal

        # with open(r'C:\\users\Fredrik\desktop\Repos\Nackademin\Programmering_Systemering\GroupAssignmentDevOps22\data\persons.csv') as f:
            # reader = csv.reader(f)
            # for row in reader:
                # print(row)

    def delete_a_person(self):                                                                                                               ## Delete OK?
        choice2 = input("Who do you want to delete?: ")
        try:
            sqliteConnection = sqlite3.connect('db\SQLiteDB.db')
            cursor = sqliteConnection.cursor()
            delete_query = ("DELETE from persons WHERE `firstname` = ?").title()
            cursor.execute(delete_query, (choice2,))
            sqliteConnection.commit()
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

    def __init__(self, greeting):
        self.greeting = greeting

    def user_input(self):
        return int(input("Enter your choice [1-4]: "))

    def menu_choice(self, choice):
        if choice == 4:
            self.running = False
        elif choice == 1:
            self.greeting.list_all_persons()
        elif choice == 2:
            self.greeting.delete_a_person()
        elif choice == 3:
            self.greeting.update_a_persons_address()

    def menu_loop(self):
        self.running = True
        while self.running:
            print(Menu.MAIN_MENU_TEXT)
            choice = self.user_input()
            self.menu_choice(choice)


if __name__ == '__main__':
    greeting = Greetings('Eva')
    Menu(greeting).menu_loop()