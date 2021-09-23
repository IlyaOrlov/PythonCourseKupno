import tempfile
import os

class WrapStrToFile:

    def __init__(self):
        self.filepath = tempfile.mktemp(suffix='.txt', dir='.')

    @property
    def content(self):
        try:
            with open(self.filepath, 'r') as f:
                data = f.read()
        except Exception:
            data = "Файл еще не существует"
        return data

    @content.setter
    def content(self, value):
        with open(self.filepath, 'w') as f:
            f.write(str(value))

    @content.deleter
    def content(self):
        print('Файл удален')
#        os.close(fd)
        os.unlink(self.filepath)


wstf = WrapStrToFile()
print(wstf.filepath)
print(wstf.content)
wstf.content = 'Привет'
print(wstf.content)
wstf.content = 'Привет еще раз'
print(wstf.content)
del wstf.content