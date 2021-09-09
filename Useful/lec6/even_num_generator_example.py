def gen_num(limit):
    i = 0
    n = 0
    while i < limit:
        a = n
        n += 2
        i += 1
        yield a

for each in gen_num(5):
   print(each)
print("============")
for each in gen_num(5):
   print(each)
