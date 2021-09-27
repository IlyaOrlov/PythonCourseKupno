def count_symbol(a):
    count = 0
    for i in test_str:
        if i == 'i':
            count = count + 1
    return count

test_str = 'Hi, Elvis, I am here!'
n = count_symbol(test_str)
print ('Символ i встречается в строке: ' + test_str + ' '+str(n)+' раз')
