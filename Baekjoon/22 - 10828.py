import sys

num = int(sys.stdin.readline().rstrip())
array = []

while num != 0:
    order = sys.stdin.readline().rstrip()

    if 'push' in order:
        array.append(order.split(' ')[1])

    elif 'pop' in order:
        if len(array) == 0:
            print(-1)
        else:
            print(array.pop())

    elif 'size' in order:
        print(str(len(array)))

    elif 'empty' in order:
        if len(array) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(array) == 0:
            print(-1)
        else:
            print(str(array[len(array)-1]))

    num -= 1