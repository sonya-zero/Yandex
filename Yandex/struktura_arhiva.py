import json

from zipfile import ZipFile

with ZipFile(input(), 'a') as myzip:
    myzip.write('test.txt')
    print(myzip.namelist())
