# s = 'z'
#
# while not s.isdigit():
#     s = input('Input digit: ')

while not (s := input('Input digit: ')).isdigit() and s != 'stop':
    pass

