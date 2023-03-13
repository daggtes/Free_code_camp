people = [
    {"name": "harry", "house": "Gryy"},
    {"name": "harry", "house": "Gryy"},
    {"name": "harry", "house": "Gryy"}
]



people.sort(key = lambda person:person["name"])

print(people)