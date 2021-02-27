import sys
data = sys.stdin.readlines()
time_table = dict()
for i in data:
    i = i.strip().split()
    if i[0] in ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота'):
        continue
    if i == "":
        continue
    if str(i[-1]).isdigit():
        if str(i[-1]) not in time_table:
            time_table[i[-1]] = []
        time_table[i[-1]].append(i[:-1])