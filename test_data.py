import json
from pprint import pprint

with open('Dictionary/test_data.json') as data_file:    
    data = json.load(data_file)

print(type(data))
print(data)
