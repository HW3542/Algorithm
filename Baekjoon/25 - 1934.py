input_num = int(input())

for _ in range(input_num):
    num1, num2 = map(int, input().split())

    max_num = max(num1, num2)
    min_num = min(num1, num2)

    while True:
        x = min_num
        y = max_num%min_num

        max_num, min_num = x,y

        if min_num == 0:
            break

    print(num1 * num2//max_num)