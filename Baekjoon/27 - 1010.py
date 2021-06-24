input_num = int(input())


def factorial(num):
    facto_num = 1
    for i in range(1, num + 1):
        facto_num = facto_num * i
    return facto_num


for _ in range(input_num):
    west, east = map(int, input().split())
    answer = factorial(east) // factorial(east - west) // factorial(west)
    print(answer)
