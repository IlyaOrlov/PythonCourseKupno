def fun(s, lst1, lst2):
    s = "123"
    lst1.append("d")
    lst2 = []


x = "abc"
y = ["a", "b", "c"]
z = ["e", "f", "g"]
fun(x, y, z)


print(x)  # abc | 123
print(y)  # abcd
print(z)  # efg


