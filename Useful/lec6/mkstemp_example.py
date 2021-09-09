import tempfile
import os


fd, path = tempfile.mkstemp(dir='.')
print(fd)
print(path)
# os.write(fd, '123'.encode())
os.close(fd)
os.unlink(path)
