def is_palindrome(a):
  a = a.lower()
  if a == a[::-1]:
    print('Данное слово является палиндромом')
  else:
    print('Данное слово не является палиндромом')

a = input('Введите слово: ')
is_palindrome(a)