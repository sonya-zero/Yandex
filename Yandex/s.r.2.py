f1 = open("files/names.txt", "r")
f2 = open("files/values.txt", "r")
f3 = open("result.txt", "w")
g = f1.readlines()
uslov = g[0].strip()
imena = g[1].split(" ")
chisla = f2.readlines()
n1 = 0
n2 = 0

for i in chisla:
    i.split(" ")
    x = int(i[0].strip())
    if eval(uslov):
        n1 = n1 + 1
    x = int(i[1].strip())
    if eval(uslov):
        n2 = n2 + 1

if n1 > n2:
    print(f"'{imena[0]}', {n1}", file="f3")
elif n2 > n1:
    print(f"'{imena[1]}', {n2}", file="f3")
else:
    print(f"'{imena[0]}', '{imena[1]}'", file="f3")

f1.close()
f2.close()
f3.close()