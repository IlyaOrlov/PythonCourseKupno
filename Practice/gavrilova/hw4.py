def check_palindrome(a):
    b = a[::-1]
    if a == b:
        print(a, "Палиндром")
    else:
        print(a, "Не палиндром")

x = input("Введите слово: ")
x = x.lower()
check_palindrome(x)