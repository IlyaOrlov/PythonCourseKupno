def count_symbol(a):
    counter = a.count('i')
    return counter

s = 'Hi, Elvis, I am here!'
s1 = count_symbol(s)
print ('Символ i встречается в строке: ' + s + ' '+str(s1)+' раз')
