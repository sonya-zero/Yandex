n = int(input())
mail = []
for i in range(n):
    mail.append(input())

m = int(input())
im = []
for i in range(m):
    im.append(input())

ind = "@untitled.py"

for i in im:
    k = 0
    for j in mail:
        if i in j:
            k = k + 1
    if k != 0:
        print(f"{i}{k}{ind}")
    else:
        print(f"{i}{ind}")