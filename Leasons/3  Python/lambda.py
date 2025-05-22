#lambda include a function as a single line
people = [
    {"name": "Harry", "house": "Griffindor"},
    {"name": "Cho", "house": "Revenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

def f(person):
    return person["name"]

people.sort(key=lambda person: person["name"])

print(people)