input_num = int(input())


def func(n):
    array = str(n)

    result = n

    for i in array:
        result += int(i)

    return result

num = 0

for j in range(1, 1000001):
    if func(j) == input_num:
        num = j
        break

print(num)
