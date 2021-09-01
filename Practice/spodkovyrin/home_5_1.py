lst = []

for i in range(1, 101):
    if i%3 == 0 and i%5 == 0:
        lst.append('FizzBuzz')
    elif i%3 == 0:
        lst.append('Fizz')
    elif i%5 == 0:
        lst.append('Buzz')
    else:
        lst.append(i)

print(lst)
