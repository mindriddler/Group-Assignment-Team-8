import csv

persons = [
    {
        "firstname": "pelle",
        "lastname": "svensson",
        "birthdate": "94-02-15",
        "address": "lillgatangatan 4"
    },
        {
        "firstname": "nina",
        "lastname": "bengtsson",
        "birthdate": "99-02-02",
        "address": "storgatan 4"
    },
        {
        "firstname": "nisse",
        "lastname": "svensson",
        "birthdate": "67-04-12",
        "address": "bergsvägen 11"
    },
        {
        "firstname": "johan",
        "lastname": "persson",
        "birthdate": "94-07-15",
        "address": "inteckningsvägen 1"
    },
        {
        "firstname": "karl",
        "lastname": "nilsson",
        "birthdate": "84-02-27",
        "address": "sedelvägen 5"
    },    
] 



# https://docs.python.org/3/library/csv.html
with open(r"C:\Users\Fredrik\Desktop\Repos\Nackademin\Programmering_Systemering\GroupAssignmentDevOps22\data\persons.csv", 'w+') as f:
    csv_writer = csv.DictWriter(f, fieldnames=persons[0].keys())
    csv_writer.writeheader()
    csv_writer.writerows(persons)