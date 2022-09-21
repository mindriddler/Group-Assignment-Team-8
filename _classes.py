import db_init

# def print_one(connection):   
#     cursor = connection.cursor()
#     result = cursor.execute('select * from persons;').fetchall()
#     return result
    

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

# def make_func_to_str_and_print(connection):
#     result = print_one(connection)
#     person_1 = Person(result[1], result[2], result[3], result[4])
#     print(person_1)



def clazz():
    with db_init.conn_to_db('db\SQLiteDB.db') as conn:
        # print("Connection to SQL open.")
        db_init.cursor(conn)
        getlimitedRows(conn, 6)
        # print_one(conn)
        # make_func_to_str_and_print(conn)
    db_init.close_connection(conn)