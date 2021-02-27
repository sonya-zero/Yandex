from random import choice

f = open("lines.txt")
data = f.readlines()
if data:
    stroka = choice(data)
    print(stroka)