num = int(input())

for i in range(num):
    array = list(map(int, input().split()))

    if array[2] % array[0] != 0:
        room = array[2] // array[0] + 1
        floor = array[2] % array[0]
    else:
        room = array[2] // array[0]
        floor = array[0]

    if room < 10:
        room_string = '0' + str(room)
    else:
        room_string = str(room)

    floor_string = str(floor)
    print(int(floor_string+room_string))