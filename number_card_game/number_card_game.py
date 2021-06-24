x, y = map(int, input().split())
number_list = []

for _ in range(x):
    number_list.append(map(int, input().split()))

array = []
for i in range(x):
    array.append(min(number_list[i]))

print(max(array))