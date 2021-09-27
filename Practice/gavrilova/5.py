def count_symbol(a, s):
    count = 0
    for i in a:
        if i == s:
            count = count + 1
    return count

test_str = 'Hi, Elvis, I am here!'
simv = 'i'
n = count_symbol(test_str, simv)
print ('Символ ' + simv + ' встречается в строке: ' + test_str + ' '+str(n)+' раз')
