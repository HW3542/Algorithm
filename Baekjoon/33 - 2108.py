import sys
from collections import Counter

input_num = int(sys.stdin.readline())

array = []

for i in range(input_num):
    i = int(sys.stdin.readline())
    array.append(i)

sum = 0
for i in array:
    sum += i

average = sum / len(array)
print(round(average))


array.sort()
print(array[(1+(len(array)-1))//2])


frequency = Counter(array)
if len(list(frequency.keys())) == 1:
    print(list(frequency.keys())[0])
else:
    if list(frequency.keys())[0] == list(frequency.keys())[1]:
        print(list(frequency.keys())[1])
    else:
        print(list(frequency.keys())[0])

print(array[-1]-array[0])