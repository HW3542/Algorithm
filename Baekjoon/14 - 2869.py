climb, slip, destination = map(int, input().split())

day = 0
day_move = climb - slip

if climb >= destination:
    print(1)
else:
    if (destination - climb) % day_move == 0:
        day = (destination - climb) // day_move + 1
    else:
        day = (destination - climb) // day_move + 2

    print(day)


