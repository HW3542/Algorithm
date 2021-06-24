n, m, k = map(int, input().split())

array = list(map(int, input().split()))

array.sort()

first = array[-1]
second = array[-2]

count = m//(k+1) * k
count += m % (k+1)

result = first * count
result += second * (m - count)
print(result)
