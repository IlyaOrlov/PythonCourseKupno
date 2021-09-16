import re


s = 0
with open('employee_info.txt', 'rb') as f:
    pattern = '- (\d+)'
    for line in f:
       line = line.decode()
       res = re.findall(pattern, line)
       if res:
           s += int(res[0])

print(s)
