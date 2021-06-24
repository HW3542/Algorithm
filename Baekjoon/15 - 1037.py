num = int(input())

divisor = list(map(int, input().split()))

max = divisor[0]
min = divisor[0]
for i in range(1, len(divisor)):
    if divisor[i] >= max:
        max = divisor[i]

for j in range(1, len(divisor)):
    if divisor[j] <= min:
        min = divisor[j]

print(max*min)