dict = {'1': 'cat', '2': 'dog'}

x = 'I have 1 and 2'

for i in dict.keys():
    x = x.replace(i, dict[i])

print(x)