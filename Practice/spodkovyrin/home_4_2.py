def is_palindrome(a):
  if a.lower()[::1] == a.lower()[::-1]:
    print('Данное слово является палиндромом')
  else:
    print('Данное слово не является палиндромом')

a = input('Введите слово: ')
is_palindrome(a)