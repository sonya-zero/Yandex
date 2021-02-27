f = open("data.txt", "r")
f2 = open("input.txt", "w")
deta = []
data = f.readlines()
for i in data:
    r = i.split(" ")
    he = []
    for j in r:
        e = 0
        t = []
        for g in j:
            if g not in t:
                t.append(g)
            else:
                e = e + 1
        if e < 1:
            he.append(j.strip())
    deta.append(he)
for i in deta:
    print(*i, file=f2)
f.close()
f2.close()