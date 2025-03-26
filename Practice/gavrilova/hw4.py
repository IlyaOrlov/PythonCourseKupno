def check_palindrome(a):
    a = a.lower()
    b = a[::-1]
    if a == b:
        print(a, "Палиндром")
    else:
        print(a, "Не палиндром")

x = input("Введите слово: ")
check_palindrome(x)