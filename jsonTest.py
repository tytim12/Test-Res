import json

data = {
    'posistion' : 'Product Manager',
    'age' : 20,
    'name' : 'Tim',
    'surname' : 'Tan'
}

json_str = json.dumps(data)
print("Python structured data:", repr(data))

data2 = json.loads(json_str)
print("data2['name']:", data2['name'])