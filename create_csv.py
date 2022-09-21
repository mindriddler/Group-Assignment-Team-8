import csv

persons = [
    {
        "Index": 1,
        "Firstname": "pelle",
        "Lastname": "svensson",
        "Birthdate": "94-02-15",
        "Address": "lillgatangatan 4"
    },
        {
        "Index": 2,
        "Firstname": "nina",
        "Lastname": "bengtsson",
        "Birthdate": "99-02-02",
        "Address": "storgatan 4"
    },
        {
        "Index": 3,
        "Firstname": "nisse",
        "Lastname": "svensson",
        "Birthdate": "67-04-12",
        "Address": "bergsvägen 11"
    },
        {
        "Index": 4,
        "Firstname": "johan",
        "Lastname": "persson",
        "Birthdate": "94-07-15",
        "Address": "inteckningsvägen 1"
    },
        {
        "Index": 5,
        "Firstname": "karl",
        "Lastname": "nilsson",
        "Birthdate": "84-02-27",
        "Address": "sedelvägen 5"
    },    
] 



# https://docs.python.org/3/library/csv.html
with open(r"C:\Users\Fredrik\Desktop\Repos\Nackademin\Programmering_Systemering\GroupAssignmentDevOps22\data\persons.csv", 'w+') as f:
    csv_writer = csv.DictWriter(f, fieldnames=persons[0].keys())
    csv_writer.writeheader()
    csv_writer.writerows(persons)