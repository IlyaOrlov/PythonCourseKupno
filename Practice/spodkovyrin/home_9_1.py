from datetime import date
import numpy as np

def work_days(d1, d2, h):
    days = np.busday_count(d1, d2, holidays=h)
    print(days + 1)

d1 = date(2021, 11, 1)
d2 = date(2021, 11, 24)
h = ['2021-11-04', '2021-11-05']
work_days(d1, d2, h)
