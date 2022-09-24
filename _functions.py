# Function to update address by quary firstname
import sqlite3
from msvcrt import getch


#################################### FUNCTIONS FOR PERSONS ####################################

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
    try:
        if search_choice == "Firstname":
            firstname_choice = input("Please enter the firstname of the person: ").title()
            search_quary = ("SELECT * FROM persons WHERE firstname = ?")
            result = cursor.execute(search_quary, (firstname_choice, )).fetchone()
            print(result[0:4])
        elif search_choice == "Lastname":
            lastname_choice = input("Please enter the lastname of the person: ").title()
            search_quary = ("SELECT * FROM persons WHERE lastname = ?")
            result = cursor.execute(search_quary, (lastname_choice, )).fetchone()
            print(result[0:4])
        elif search_choice == "Address":
            address_choice = input("Please enter the address of the person: ").title()
            search_quary = ("SELECT * FROM persons WHERE address = ?")
            result = cursor.execute(search_quary, (address_choice, )).fetchone()
            print(result[0:4])
        elif search_choice == "Birthdate":
            birthdate_choice = str(input("Please enter the birthdate of the person formated as such; 'YY-MM-DD': "))
            search_quary = ("SELECT * FROM persons WHERE birthdate = ?")
            result = cursor.execute(search_quary, (birthdate_choice, )).fetchone()
            print(result[0:4])
        else:
            print("Your choice did not make any sense for us, please try again.")
    except TypeError:
        print("Entry dosn't exist in database.")
        
        
#################################### FUNCTIONS FOR VEHICLES ####################################

def delete_vehicle():
    delete_choice = input("Please specify the registration number of the car you want to delete?: ").upper()
    
    try:
        sqliteConnection = sqlite3.connect('db\SQLiteDB.db')
        cursor = sqliteConnection.cursor()
        delete_query = ("DELETE from vehicles WHERE regnr = ?")
        cursor.execute(delete_query, (delete_choice, ))
        sqliteConnection.commit()
        print("Entry Deleted")
        cursor.close()
    except AttributeError:
            print("No object to delete")
            
def connect_to_db():
    conn = sqlite3.connect('db\SQLiteDB.db')
    return conn

def add_vehicles():   
    conn = sqlite3.connect('db\SQLiteDB.db')
    
    vehicle_manu = input("Enter the vehicles manufacturer: ").title()
    vehicle_model = input("Enter the vehicles model: ").title()
    if vehicle_model == "Xc90":
        vehicle_model = vehicle_model.upper()
    vehicle_color = input("Enter the vehicles color: ").lower()
    vehicle_regnr = input("Enter the vehicles registration number: ").upper()
    vehicle_owner = input("Enter the vehicles owner(both firstname and lastname):  ").title()
    
    conn.execute('CREATE TABLE IF NOT EXISTS vehicles (manufacturer, model, color, regnr, owner, CONSTRAINT regnr_unique UNIQUE (regnr));')
    conn.execute('INSERT OR REPLACE INTO vehicles (manufacturer, model, color, regnr, owner) VALUES (?, ?, ?, ?, ?);', (vehicle_manu, vehicle_model, vehicle_color, vehicle_regnr, vehicle_owner, ))
    conn.commit()
    connect_to_db().close()
    print("Entry created.")
    
def list_all_vehicles():
    result = connect_to_db().execute('SELECT * FROM vehicles').fetchall()
    for all in result:
        print(all)

def query_vehicle_with_():

    conn = sqlite3.connect('db\SQLiteDB.db')
    cursor = conn.cursor()
    
    sql = '''SELECT manufacturer, model, color, regnr, owner
            FROM vehicles
            INNER JOIN persons
            ON vehicles.owner = persons.fullname;'''
    
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

#################################### FUNCTION WAIT FOR KEYPRESS ####################################
def wait():
    print("\nPress any key to continue ...", end="")
    getch()