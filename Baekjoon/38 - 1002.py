num = int(input())

for _ in range(num):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    if ((x2-x1)**2 + (y2-y1)**2)**0.5 > r1 + r2:
        print(0)
    elif ((x2-x1)**2 + (y2-y1)**2)**0.5 == r1 + r2:
        print(1)
    elif ((x2-x1)**2 + (y2-y1)**2)**0.5 == 0:
        if r1 != r2:
            print(0)
        else:
            print(-1)
    elif ((x2-x1)**2 + (y2-y1)**2)**0.5 == abs(r1 - r2):
        print(1)
    elif ((x2-x1)**2 + (y2-y1)**2)**0.5 < abs(r1 - r2):
        print(0)
    else:
        print(2)