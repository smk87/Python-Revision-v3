# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary
import json

# Sample JSON
userJSON = '{"first_name": "John", "last_name": "Doe","age": 30}'

# Parse JSON to dict
user = json.loads(userJSON)

print(user)
print(user['last_name'])

car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}

# Parse dict to JSON
carJSON = json.dumps(car)

print(carJSON)
