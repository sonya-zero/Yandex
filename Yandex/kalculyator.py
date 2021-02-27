import sys


try:
    print(int(sys.argv[1]) + int(sys.argv[2]))
except Exception as ex:
    print(0)