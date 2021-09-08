import tempfile
import os

class WrapStrToFile:

    def __init__(self, filepath):
        self.filepath = filepath

    @property
    def content(self):
        with open(self.filepath, 'r') as f:
            try:
                r = f.read()
            except Exception:
                print("File doesn't exist")
            return f'{r}'

    @content.setter
    def content(self, value):
        with open(self.filepath, 'w') as f:
            f.write(str(value))

    @content.deleter
    def content(self):
        self.filepath = 'Deleted'


fd, path = tempfile.mkstemp(suffix='.txt', dir='E:\Study\PythonCourseKupno\Practice\spodkovyrin', text=True)
wstf = WrapStrToFile(path)
print(wstf.content)
wstf.content = 'test str'
print(wstf.content)
wstf.content = 'text 2'
print(wstf.content)
del wstf.content
os.close(fd)
os.unlink(path)
