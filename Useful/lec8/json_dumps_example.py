import json


my_list = [{'Ivanov': ('Ivan', 10000)}, {'Petrov': ('Petr', 20000)}]
my_json_str = json.dumps(my_list)
print(f'my_json_str: {my_json_str}')
with open('myfile', 'w') as f:
    f.write(my_json_str)

