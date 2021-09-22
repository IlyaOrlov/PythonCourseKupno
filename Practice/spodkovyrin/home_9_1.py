from datetime import date, timedelta


def work_days(d1, d2):
    days = (d1 + timedelta(x + 1) for x in range((d2 - d1).days))
    print(sum(1 for day in days if day.weekday() < 5) + 1)


d1 = date(2021, 9, 17)
d2 = date(2021, 9, 26)
work_days(d1, d2)
