import tempfile
import os

class WrapStrToFile:

    def __init__(self):
        self.filepath = tempfile.mktemp(suffix='.txt')

    @property
    def content(self):
        try:
            with open(self.filepath, 'r') as f:
                r = f.read()
        except Exception:
            r = "File doesn't exist"
        return r

    @content.setter
    def content(self, value):
        with open(self.filepath, 'w') as f:
            f.write(str(value))

    @content.deleter
    def content(self):
        print('File Deleted')
        os.unlink(self.filepath)


wstf = WrapStrToFile()
print(wstf.filepath)
print(wstf.content)
wstf.content = 'test str'
print(wstf.content)
wstf.content = 'text 2'
print(wstf.content)
del wstf.content
