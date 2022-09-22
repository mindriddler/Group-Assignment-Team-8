import db_init

def go_fetch_all(connection):   
    cursor = connection.cursor()
    result = cursor.execute('select * from persons;').fetchall()
    return result

class Person:
    
    def __init__(self, firstname, lastname, birthdate, address):
        # self.index = index
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.address = address
     
    def __str__(self):
        return f"{self.firstname} {self.lastname} is born {self.birthdate} and lives on {self.address}"

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