import sys
number = int(input())
price = dict()
orders = list()
order = 0
for i in range(number):
    data = input().split('\t')
    price[data[0]] = int(data[1])
input()
data = input()
while data != ".":
    if data != "":
        data = data.split('\t')
        order += price[data[0]] * int(data[1].strip())
    else:
        orders.append(order)
        order = 0
    data = input()
orders.append(order)
count = 1
for i in orders:
    if i:
        print(f'{count}) {i}')
        count += 1
print('Итого:', sum(orders))