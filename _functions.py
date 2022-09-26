# Function to update address by quary firstname
import sqlite3
from msvcrt import getch


#################################### FUNCTIONS FOR PERSONS ####################################

# This is the function that the person class is using to get it's result back so it can start creating class objects
def go_fetch_all():   
    conn = sqlite3.connect('db\SQLiteDB.db')
    cursor = conn.cursor()
    result = cursor.execute('select * from persons;').fetchall()
    return result

# function to update a entrys address in the datebase
def update_db():
    # Choice of firstname to update (casesensetive hence .title())
    sqliteConnection = sqlite3.connect('db\SQLiteDB.db')
    cursor = sqliteConnection.cursor()
    update_person = input("Insert fullname of the person you want to change address for: ").title()
    cursor.execute("SELECT rowid FROM persons WHERE fullname = ?", (update_person,))
    data = cursor.fetchall()
    if len(data) == 0:
        print("That entry doesn't exist in the database.")
    else:
        update_address = input("Insert new addres: ").title()
        update_quary = ("UPDATE persons SET address = ? WHERE fullname = ?")   
        cursor.execute(update_quary, (update_address, update_person))
        sqliteConnection.commit()
        print("Address updated")
        cursor.close()

# function to delete a entry in the database based on the fullname of a person
def delete_a_person():                                                                                                             
    delete_choice = input("Please specify the fullname of the entry you want to delete: ").title()
    
    sqliteConnection = sqlite3.connect('db\SQLiteDB.db')
    cursor = sqliteConnection.cursor()   
    cursor.execute("SELECT rowid FROM persons WHERE fullname = ?", (delete_choice,))
    data = cursor.fetchall()
    if len(data) == 0:
        print("That name doesn't exist in the database.")
    else:
        delete_query = ("DELETE from persons WHERE fullname = ?")
        cursor.execute(delete_query, (delete_choice, ))
        sqliteConnection.commit()
        cursor.close()
        print("Entry deleted.")   

# This function allows the user to search the database and get returned a result that matches thier specifications.
# if user searches for a specific firstname, then all entrys what that firstname get printed
# Lift question to Martin regarding fetchone and fetchall when there is specific
def query_persons_with_():
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
            print("Sorry, i did not understand your choice. Please try again.")
    except TypeError:
        print("Entry doesn't exist in database.")
        
        
#################################### FUNCTIONS FOR VEHICLES ####################################

# Same as above delete function, but this time for the vehicle table
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

# Not sure if we need this function seeing as we mostly just connect in each function. Will investigate tomorrow           
def connect_to_db():
    conn = sqlite3.connect('db\SQLiteDB.db')
    return conn

# Here we allow the user to input entrys into the vehicle database with different specifications
def add_vehicles():   
    conn = sqlite3.connect('db\SQLiteDB.db')
    
    vehicle_manu = input("Enter the vehicles manufacturer: ").title()
    vehicle_model = input("Enter the vehicles model: ").title()
    if vehicle_model == "Xc90":
        vehicle_model = vehicle_model.upper()
    vehicle_color = input("Enter the vehicles color: ").lower()
    vehicle_regnr = input("Enter the vehicles registration number: ").upper()
    vehicle_owner = input("Enter the vehicles owner(both firstname and lastname): ").title()
    
    conn.execute('CREATE TABLE IF NOT EXISTS vehicles (manufacturer, model, color, regnr, owner, CONSTRAINT regnr_unique UNIQUE (regnr));')
    conn.execute('INSERT OR REPLACE INTO vehicles (manufacturer, model, color, regnr, owner) VALUES (?, ?, ?, ?, ?);', (vehicle_manu, vehicle_model, vehicle_color, vehicle_regnr, vehicle_owner,))
    conn.commit()
    connect_to_db().close()
    print("Entry created.")

# Listing all the entrys in the vehicle table
def list_all_vehicles():
    result = connect_to_db().execute('SELECT * FROM vehicles').fetchall()
    for all in result:
        print(all)
        
# This function is hte one that Car_owner is using the find a person that owns a specific car and print that 
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