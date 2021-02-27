t = input()
s = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
st = "qwertyuiopasdfghjklzxcvbnm"


def poisk(t):
    err = 0
    if t[0] == "+":
        if t[1] == "7":
            pass
        pass

    if t[1] == "8":
        pass
    
    if t[-1] == "-":
        err = err + 1

    for i in range(len(t)):
        if t[i] == " ":
            pass
        if t[i] == "-":
            if t[-1] == "-":
                err = err + 1
            elif t[i + 1] == "-":
                err = err + 1
        if t[i] in st:
            err = err + 1

    if "(" in t or ")" in t:
        cou = 0
        cuo = 0
        for i in t:
            if i == "(":
                cou = cou + 1
        for i in t:
            if i == ")":
                cuo = cuo + 1
        if cou == 1 and cuo == 1:
            if t.find("(") < t.find(")"):
                pass
            else:
                err = err + 1

    return err


n = ""
if poisk(t) == 0:
    for i in t:
        if i in s:
            n = n + i
    print(f"+7{n[1:]}")
else:
    print("error")