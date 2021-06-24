num = int(input())

def hanoi(num, start, medium, to):
    if num == 1:
        print(start,to)
        return
    hanoi(num-1, start, to, medium)
    print(start,to)
    hanoi(num-1, medium, start, to)


hanoi(num, 1, 2, 3)