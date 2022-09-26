from _functions import query_vehicle_with_, go_fetch_all

# Person class.
# This will call a function that initiate a query and a fetchall from the database which then get back here, remade from tuples to list and then iterated over and over based on how many entrys the fetchall returns.
# each round in the for loop will create a object that gets printed to the terminal
class Person:
    
    def __init__(self, firstname, lastname, birthdate, address):
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.address = address

    def __str__(self):
        return f"{self.firstname} {self.lastname} is born {self.birthdate} and lives on {self.address}"

    def people_print():
        try:
            
            fetch_all_result = go_fetch_all()
            lst_of_lst = list(map(list, fetch_all_result))
            len_of_lst_of_lst = len(lst_of_lst)
            
            for i in range(len_of_lst_of_lst):
                person = lst_of_lst[i]
                person_finished = Person(person[0], person[1], person[2], person[3])
                print(person_finished)
        except IndexError as error:
            print("Woops -", error)
            
            
# vehicle class.
# This is abit different.
# instead of querying and fetchall, this will initiate a function that looks for similarities between vehicles table and persons table and
# the returned result from that fetch from the database will get printed, if the query finds no matching results then nothing get printed         
class Car_owned:
    
    def __init__(self, manufacturer, model, color, regnr, owner):
        self.manufacturer = manufacturer
        self.model = model
        self.color = color
        self.regnr = regnr
        self.owner = owner

    def __str__(self):
        return f"The owner of the {self.color} {self.manufacturer} {self.model} with registration number {self.regnr} is {self.owner}"

    def car_print():
        try:
            
            fetch_all_result = query_vehicle_with_()
            lst_of_lst = list(map(list, fetch_all_result))
            len_of_lst_of_lst = len(lst_of_lst)
            
            for i in range(len_of_lst_of_lst):
                vehicle = lst_of_lst[i]
                vehicle_finished = Car_owned(vehicle[0], vehicle[1], vehicle[2], vehicle[3], vehicle[4])
                print(vehicle_finished)
        except IndexError as error:
            print("Woops -", error)