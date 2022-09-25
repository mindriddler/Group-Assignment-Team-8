import csv

persons = [
        {
        "Firstname": "Pelle",
        "Lastname": "Svensson",
        "Birthdate": "94-02-15",
        "Address": "Lillgatan 4",
        "Fullname": "Pelle Svensson"
    },
        {
        "Firstname": "Nina",
        "Lastname": "Bengtsson",
        "Birthdate": "99-02-02",
        "Address": "Storgatan 4",
        "Fullname": "Nina Bengtsson"
    },
        {
        "Firstname": "Nisse",
        "Lastname": "Svensson",
        "Birthdate": "67-04-12",
        "Address": "Bergsvägen 11",
        "Fullname": "Nisse Svensson"
    },
        {
        "Firstname": "Johan",
        "Lastname": "Persson",
        "Birthdate": "94-07-15",
        "Address": "Inteckningsvägen 1",
        "Fullname": "Johan Persson"
    },
        {
        "Firstname": "Karl",
        "Lastname": "Nilsson",
        "Birthdate": "84-02-27",
        "Address": "Sedelvägen 5",
        "Fullname": "Karl Nilsson"
    },    

] 


# creating out csv file 
def create_csv():
    with open('data\persons.csv', 'w', encoding='UTF-8', newline='') as f:
        # writer = csv.writer(csvarchive)
        csv_writer = csv.DictWriter(f, fieldnames=persons[0].keys())
        csv_writer.writeheader()
        csv_writer.writerows(persons)