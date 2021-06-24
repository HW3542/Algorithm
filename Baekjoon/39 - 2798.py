num1, num2 = map(int, input().split())

card = list(map(int, input().split()))

sum_max = 0

card.sort()


for i in range(len(card)-2):
    sum = 0
    sum += card[i]
    for j in range(i+1, len(card)-1):
        sum = card[i]
        sum += card[j]
        if num2 - sum < card[j+1]:
            break
        for k in range(j+1, len(card)):
            sum = card[i] + card[j]
            sum += card[k]
            if sum > num2:
                break
            elif sum >= sum_max:
                sum_max = sum

print(sum_max)