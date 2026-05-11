import json
data = {'name': 'parth', 'age': 26, 'city': 'ahm'}
with open('data.json', 'w') as file:
    json.dump(data, file)
