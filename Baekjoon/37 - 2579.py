import sys

num = int(input())

stair = []
dp = []

for _ in range(num):
    input_stair = int(sys.stdin.readline())
    stair.append(input_stair)

if len(stair) == 1:
    dp.append(stair[0])
elif len(stair) == 2:
    dp.append(max(stair[0] + stair[1], stair[1]))
elif len(stair) == 3:
    dp.append(max(stair[0] + stair[2], stair[1] + stair[2]))
else:
    dp.append(stair[0])
    dp.append(max(stair[0] + stair[1], stair[1]))
    dp.append(max(stair[0] + stair[2], stair[1] + stair[2]))
    for i in range(3, num):
        dp.append(max(dp[i - 2] + stair[i], dp[i - 3] + stair[i - 1] + stair[i]))

print(dp.pop())