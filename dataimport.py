import json

with open(r"c:\users\fredr\desktop\Repos\Nackademin\Programmering_Systemering\GroupAssignmentDevOps22\data\persons.json") as f:
    data_to_database_executemany = []
    persons = json.load(f)
    for person in persons['persons']:
        data_to_database_executemany.append(tuple(person.values()))

print(data_to_database_executemany)
