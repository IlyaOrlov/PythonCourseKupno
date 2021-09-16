import json


with open('myfile', 'r') as f:
    s = f.read()
    s2 = json.loads(s)
    print(s2)

    print(type(s2))
