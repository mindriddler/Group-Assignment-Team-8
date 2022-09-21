import sqlite3
from db_insert import db_path
from db_insert import cursor
from db_insert import sqliteConnection


sqliteConnection = sqlite3.connect(db_path)
cursor = sqliteConnection.cursor()
    
# Show the table
cursor.execute('select * from persons;')

# cursor.execute("INSERT INTO persons VALUES (?, ?, ?, ?)", (person_1.firstname, person_1.lastname, person_1.birthdate, person_1.address))

# sqliteConnection.commit()
# View result. Remove comment to print data from the DB
result = cursor.fetchone()




class Person:
    
    def __init__(self,index, firstname, lastname, birthdate, address):
        self.index = index
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.address = address
     
    
        
    def __str__(self):
        return f"{self.index}, {self.firstname} {self.lastname} is born {self.birthdate} and lives on {self.address}"


person_1 = Person(result[0], result[1], result[2], result[3], result[4])
print(person_1)




"""class Person:
    def init(self,index, first, last, birth, address):
        self.index = index
        self.first = first
        self.last = last
        self.birth = birth
        self.address = address

    def str(self):
        return f"{self.index}: {self.first} {self.last}, born {self.birth}, living on {self.address}"""