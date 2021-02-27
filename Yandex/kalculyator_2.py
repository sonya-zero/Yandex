import sys

if len(sys.argv) == 1:
    print("NO PARAMS")
else:
    t = 0
    try:
        for i in range(1, len(sys.argv)):
            if i % 2 != 0:
                t += int(sys.argv[i])
            else:
                t -= int(sys.argv[i])
        print(t)
    except Exception as ex:
        print(ex.__class__.__name__)
