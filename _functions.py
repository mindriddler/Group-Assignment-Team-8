# Function to update address by quary firstname
import sqlite3
from unittest import registerResult

def update_db():
    # Choice of firstname to update (casesensetive hence .title())
    update_person = input("Insert firstname of the person you want to change address for: ").title()

    # Choice of new address
    update_address = input("Insert new addres: ").title()

    try:
        sqliteConnection = sqlite3.connect('db\SQLiteDB.db')
        cursor = sqliteConnection.cursor()
        update_quary = ("UPDATE persons SET address = ? WHERE firstname= ?")
        cursor.execute(update_quary, (update_address, update_person))
        sqliteConnection.commit()
        print("Address updated")
        cursor.close()

    except AttributeError:
        print("Something went wrong")
        

def delete_a_person():                                                                                                             
    delete_choice = input("Who do you want to delete?: ").title()
    
    try:
        sqliteConnection = sqlite3.connect('db\SQLiteDB.db')
        cursor = sqliteConnection.cursor()
        delete_query = ("DELETE from persons WHERE firstname = ?")
        cursor.execute(delete_query, (delete_choice, ))
        sqliteConnection.commit()
        print("Entry Deleted")
        cursor.close()
    except AttributeError:
            print("No object to delete")
            
            
def quary_persons_with_():
    search_choice = input("What do you want to search by? Enter either firstname, lastname, address or birthdate: ").title()
    
    conn = sqlite3.connect('db\SQLiteDB.db')
    cursor = conn.cursor()
    if search_choice == "Firstname":
        firstname_choice = input("Please enter the firstname of the person: ").title()
        search_quary = ("SELECT * FROM persons WHERE firstname = ?")
        result = cursor.execute(search_quary, (firstname_choice, )).fetchone()
        print(result)
    elif search_choice == "Lastname":
        lastname_choice = input("Please enter the lastname of the person: ").title()
        search_quary = ("SELECT * FROM persons WHERE lastname = ?")
        result = cursor.execute(search_quary, (lastname_choice, )).fetchone()
        print(result)
    elif search_choice == "Address":
        address_choice = input("Please enter the address of the person: ").title()
        search_quary = ("SELECT * FROM persons WHERE address = ?")
        result = cursor.execute(search_quary, (address_choice, )).fetchone()
        print(result)
    elif search_choice == "Birthdate":
        try:
            birthdate_choice = str(input("Please enter the birthdate of the person formated as such; 'YY-MM-DD': "))
            search_quary = ("SELECT * FROM persons WHERE birthdate = ?")
            result = cursor.execute(search_quary, (birthdate_choice, )).fetchone()
            print(result)
        except None:
            print("Something went wrong")
    else:
        print("Your choice did not make any sense for us, please try again.")