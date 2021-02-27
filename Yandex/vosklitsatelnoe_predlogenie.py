import sys
povest = set()
voskl = set()
vopros = set()
data = sys.stdin.read().replace("\n", " ").split()
temp = set()
for x in data:
    if x[-1] not in (".", "!", "?"):
        temp.add(x.lower())
    else:
        if x[-1] == ".":
            temp.add(x[0:-1].lower())
            povest |= temp
            temp.clear()
        elif x[-1] == "!":
            temp.add(x[0:-1].lower())
            voskl |= temp
            temp.clear()
        elif x[-1] == "?":
            temp.add(x[0:-1].lower())
            vopros |= temp
            temp.clear()
temp = povest & vopros
temp -= voskl
temp = sorted(temp)
print(*temp)