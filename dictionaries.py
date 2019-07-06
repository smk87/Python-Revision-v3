# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Simple Dic
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

# Using cons
person2 = dict(
    first_name="Saqlain",
    last_name="Khan",
    age=23
)
print(person2)

# Acces value
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '555-555-5555'

# Get keys
print(person.keys())

# Get value
print(person.items())

# Make a copy
person2 = person.copy()
person2['city'] = "Boston"

# Remove item
del(person['age'])
person.pop('phone')

# Clear
person.clear()

# Get len
print(len(person2))

# List of Dic
people = [
    {'name': 'Martha', "age": 40},
    {'name': 'Bob', 'age': 20}
]
print(people[1]['age'])

print(person)
