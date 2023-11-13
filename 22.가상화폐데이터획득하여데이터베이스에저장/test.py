import datetime

today = datetime.date.today()
# today
# datetime.date(2023,11,13)

diff_days = datetime.timedelta(days=100)
# diff_days
# datetime.timedelta(days=100)
# print(diff_days)

#오늘부터 100일 이후
c = today + diff_days
print(c)

#오늘부터 100일 이전
d = today - diff_days
print(d)

