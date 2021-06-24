num = int(input())
dot_array = []

for i in range(num):
    x, y = map(int, input().split())
    dot_array.append([y, x])

dot_array.sort()
print(dot_array)
for y,x in dot_array:
    print(x,y)
