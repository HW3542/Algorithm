import math

def isPrime(num):
    for i in range(2, int(math.sqrt(num)) + 1): # 합성수의 성질: 2부터 해당 수의 제곱근까지의 범위의 정수 중에 나누어지는 수가 있다.
        if num % i == 0: return False
    return True


input_limimt = list(range(1, 123456*2+1))
prime_list = []
for i in input_limimt:
    if isPrime(i):
        prime_list.append(i)

while(1):
    count = 0
    num = int(input())
    if num == 0: break

    for i in prime_list:
        if num < i <= num*2:
            count += 1

    print(count)