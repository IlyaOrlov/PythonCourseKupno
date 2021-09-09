import tempfile
import os

class WrapStrToFile:

    def __init__(self, filepath):
        self.filepath = filepath

    @property
    def content(self):
        try:
            with open(self.filepath, 'r') as f:
                r = f.read()
        except Exception:
            return "File doesn't exist"
        return r

    @content.setter
    def content(self, value):
        with open(self.filepath, 'w') as f:
            f.write(str(value))

    @content.deleter
    def content(self):
        print('File Deleted')
        os.unlink(self.filepath)


path = tempfile.mktemp(suffix='.txt', dir='E:\Study\PythonCourseKupno\Practice\spodkovyrin')
wstf = WrapStrToFile(path)
print(wstf.content)
wstf.content = 'test str'
print(wstf.content)
wstf.content = 'text 2'
print(wstf.content)
del wstf.content
