import math

a, b = map(int, input().split())

for i in range(a, b+1):
    if i == 1:
        continue
    is_prime = True
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i)