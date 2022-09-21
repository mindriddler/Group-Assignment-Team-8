import csv

persons = [
    {
        "id": 1,
        "Firstname": "Pelle",
        "Lastname": "Svensson",
        "Birthdate": "94-02-15",
        "Address": "Lillgatan 4"
    },
        {
        "id": 2,
        "Firstname": "Nina",
        "Lastname": "Bengtsson",
        "Birthdate": "99-02-02",
        "Address": "Storgatan 4"
    },
        {
        "id": 3,
        "Firstname": "Nisse",
        "Lastname": "Svensson",
        "Birthdate": "67-04-12",
        "Address": "Bergsvägen 11"
    },
        {
        "id": 4,
        "Firstname": "Johan",
        "Lastname": "Persson",
        "Birthdate": "94-07-15",
        "Address": "Inteckningsvägen 1"
    },
        {
        "id": 5,
        "Firstname": "Karl",
        "Lastname": "Nilsson",
        "Birthdate": "84-02-27",
        "Address": "Sedelvägen 5"
    },    
] 
def create_csv():
    with open('data\persons.csv', 'w', encoding='UTF-8', newline='') as f:
        # writer = csv.writer(csvarchive)
        csv_writer = csv.DictWriter(f, fieldnames=persons[0].keys())
        csv_writer.writeheader()
        csv_writer.writerows(persons)