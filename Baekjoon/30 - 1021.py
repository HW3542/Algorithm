def left_move(array):
    array.append(array.pop(0))


def right_move(array):
    array.insert(0, array.pop())


input_num1, input_num2 = map(int, input().split())
pop_list = list(map(int, input().split()))

queue_array = []

for i in range(1, input_num1 + 1):
    queue_array.append(i)

count = 0
for j in range(len(pop_list)):
    left_count = 0
    right_count = 0

    if pop_list[j] == queue_array[0]:
        queue_array.pop(0)
        break

    test_array = queue_array[:]

    while pop_list[j] != test_array[0]:
        left_move(test_array)
        left_count += 1

    test_array = queue_array[:]

    while pop_list[j] != test_array[0]:
        right_move(test_array)
        right_count += 1

    if left_count >= right_count:
        while pop_list[j] != queue_array[0]:
            right_move(queue_array)
            count += 1
        queue_array.pop(0)
    else:
        while pop_list[j] != queue_array[0]:
            left_move(queue_array)
            count += 1
        queue_array.pop(0)

print(count)