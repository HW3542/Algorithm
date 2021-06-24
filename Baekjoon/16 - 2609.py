a, b = map(int, input().split())

num1 = max(a, b)
num2 = min(a, b)

while num2 > 0:
    num1 = num1 % num2
    num1, num2 = num2, num1

print(num1)
print(a*b//num1)