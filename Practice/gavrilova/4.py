def to_title(a):
#   return a.title()
    t = a.split(' ')
    for i in range(1, len(t)):
        t[i] = t[i][0].upper() + t[i][1:]
    return ' '.join(t)

s = 'orlov Ilya evgenyevich'
print (s)
s1 = to_title(s).capitalize()
print (s1)
