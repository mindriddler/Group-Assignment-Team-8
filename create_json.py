import json

persons = {
    "persons": [{
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

}


with open(r'C:\\users\fredr\desktop\Repos\Nackademin\Programmering_Systemering\GroupAssignmentDevOps22\data\persons.json', 'w') as f:
    f.write(json.dumps(persons, indent=4))