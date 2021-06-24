input_num = int(input())

cnt = 0
six_number = 666

while True:
    if '666' in str(six_number):
        cnt += 1
    if cnt == input_num:
        print(six_number)
        break
    six_number += 1