def is_palindrome(a):
  b = a.lower()[::-1]
  if a.lower() == b:
    print('Данное слово является палиндромом')
  else:
    print('Данное слово не является палиндромом')

a = input('Введите слово: ')
is_palindrome(a)