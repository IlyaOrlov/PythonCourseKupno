lst = []

for x in range(1, 101):
    if x%3 == 0 and x%5 == 0:
        lst.append('FizzBuzz')
    elif x%3 == 0:
        lst.append('Fizz')
    elif x%5 == 0:
        lst.append('Buzz')
    else:
        lst.append(x)

print(lst)