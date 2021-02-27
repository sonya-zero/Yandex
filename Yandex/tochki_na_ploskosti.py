n = int(input())
s = []

for i in range(n):
    s.append(input())

s1 = []
s2 = []

for i in s:
    i1 = i.split(" ")
    if i1[0] == "0" or i1[1] == "0":
        s1.append(i)
    else:
        s2.append(i)

s01 = []

for i in s1:
    i = i.split(" ")
    i1 = f"({i[0]}, {i[1]})"
    s01.append(i1)

s02 = []
k1 = 0
k2 = 0
k3 = 0
k4 = 0

for i in s2:
    i1 = i.split(' ')
    if int(i1[0]) > 0 and int(i1[1]) > 0:
        k1 = k1 + 1
    elif int(i1[0]) < 0 and int(i1[1]) > 0:
        k2 = k2 + 1
    elif int(i1[0]) < 0 and int(i1[1]) < 0:
        k3 = k3 + 1
    else:
        k4 = k4 + 1

for i in s01:
    print(i)

print(f"I: {k1}, II: {k2}, III: {k3}, IV: {k4}.")