import json


import requests


data = json.load(open("serv.json"))
server = data["server"]
port = data["port"]
x_server = f"http://{server}:{port}"
params = ""

response = requests.get(x_server)
data_prim = response.json()["primitive"]
data_h_org = response.json()["highly_organized"]

average = (sum(data_prim) + sum(data_h_org)) / (len(data_prim) + len(data_h_org))
data_prim2 = round(sum([(i - average) ** 2 for i in data_prim]), 3)
data_h_org2 = round(sum([(i - average) ** 2 for i in data_h_org]), 3)

if data_prim2 < data_h_org2:
    print("primitive", data_prim2)
elif data_prim2 > data_h_org2:
    print("highly_organized", data_h_org2)
else:
    print("Same", 0)