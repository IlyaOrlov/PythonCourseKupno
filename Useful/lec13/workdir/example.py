def fun(a, b):
    return a * b


def copyfun(src, dst):
    with open(src, 'r') as fin, open(dst, 'w') as fout:
        fout.write(fin.read())

