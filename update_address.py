# Function to update address by quary firstname
import sqlite3

def update_db():
    # Choice of firstname to update (casesensetive hence .title())
    update_person = input("Insert firstname of the person you want to change address for: ").title()

    # Choice of new address
    update_address = input("Insert new addres: ").title()

    try:
        sqliteConnection = sqlite3.connect(r"db\SQLiteDB.db")
        cursor = sqliteConnection.cursor()
        update_quary = ("UPDATE persons SET address = ? WHERE firstname= ?")
        cursor.execute(update_quary, (update_address, update_person))
        sqliteConnection.commit()
        print("Address updated")
        cursor.close()

    except AttributeError:
        print("Something went wrong")