import db_init

def go_fetch_all(connection):   
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
            
            fetch_all_result = go_fetch_all(connection)
            lst_of_lst = list(map(list, fetch_all_result))
            len_of_lst_of_lst = len(lst_of_lst)
            
            for i in range(len_of_lst_of_lst):
                person = lst_of_lst[i]
                person_finished = Person(person[1], person[2], person[3], person[4])
                print(person_finished)
        except IndexError as error:
            print("Woops -", error)
        
        
def clazz():
    with db_init.conn_to_db('db\SQLiteDB.db') as conn:
        db_init.cursor(conn)
        Person.people_print(conn)
    # db_init.close_connection(conn)