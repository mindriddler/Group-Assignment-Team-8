import db_init

def print_one(connection):   
    cursor = connection.cursor()
    result = cursor.execute('select * from persons;').fetchall()
    return result
    
# This code is not used for anything, but dont delete, i like how its implemented and i want to keep it
# for future reference
def getlimitedRows(connection, size):
    
        cursor = connection.cursor()

        sqlite_select_query = 'SELECT * from persons'
        cursor.execute(sqlite_select_query)
        records = cursor.fetchmany(size)
        print("Fetching a total of", size,"rows")
        print("Printing each row")
        for row in records:
            print("\n")
            print("Firstname:", row[1])
            print("Lastname:", row[2])
            print("Birthdate:", row[3])
            print("Address:", row[4])
            print("\n")

class Person:
    
    def __init__(self, firstname, lastname, birthdate, address):
        # self.index = index
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.address = address
     
    def __str__(self):
        return f"{self.firstname} {self.lastname} is born {self.birthdate} and lives on {self.address}"

    # This code is absolut GARBAGE.... But its right now 01:34 and i need to go to bed.
    # Will try to find a way to make it look better, but im not sure.. 
    # It works now as it should anyway and it looks better than before.
    def people_print(connection):
        try:
            
            result1 = print_one(connection)
            result2 = list(map(list, result1))
        
            p2p_1 = result2[0]
            p2p_2 = result2[1]
            p2p_3 = result2[2]
            p2p_4 = result2[3]
            p2p_5 = result2[4]
            
            person_1 = Person(p2p_1[1], p2p_1[2], p2p_1[3], p2p_1[4])
            person_2 = Person(p2p_2[1], p2p_2[2], p2p_2[3], p2p_2[4])
            person_3 = Person(p2p_3[1], p2p_3[2], p2p_3[3], p2p_3[4])
            person_4 = Person(p2p_4[1], p2p_4[2], p2p_4[3], p2p_4[4])
            person_5 = Person(p2p_5[1], p2p_5[2], p2p_5[3], p2p_5[4])
            
            print(person_1)
            print(person_2)
            print(person_3)
            print(person_4)
            print(person_5)
        except IndexError as error:
            print("Woops -", error)
        
        
def clazz():
    with db_init.conn_to_db('db\SQLiteDB.db') as conn:
        db_init.cursor(conn)
        Person.people_print(conn)
    # db_init.close_connection(conn)