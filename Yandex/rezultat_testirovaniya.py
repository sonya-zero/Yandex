import json


data = json.load(open('scoring.json'))
point = 0
for i in data['scoring']:
    for j in i['required_tests']:
        if input() == "ok":
            point = point + i['points'] / len(i['required_tests'])

print(int(point))