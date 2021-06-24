import sys

input_num = int(input())

array = [0]
save_num = 0

num_list = []
for _ in range(input_num):
    num = int(sys.stdin.readline().rstrip())
    num_list.append(num)

    if array[-1] < num:
        while array[-1] < num:
            save_num += 1
            array.append(save_num)

    while array[-1] >= num:
        array.pop()


if save_num > input_num:
    print('NO')
else:
    save_num = 1
    for num in num_list:
        if array[-1] < num:
            while array[-1] < num:
                array.append(save_num)
                save_num += 1
                print('+')

        while array[-1] >= num:
            array.pop()
            print('-')
