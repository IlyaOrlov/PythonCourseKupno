from subprocess import run, PIPE
import tempfile
import os


def fun(path):
    proc = run(['type', path], shell=True, stdout=PIPE, stderr=PIPE, encoding='utf-8')
    if proc.returncode:
        print(proc.stderr)
    print('result: ', proc.stdout)


path = tempfile.mktemp(suffix='.txt', dir='.')
print(path)
with open(path, 'w') as f:
    f.write(input('Введите текст: '))

fun(path)
os.remove(path)
