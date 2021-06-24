import sys

input_num = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(input_num)]

result = []

def solution(x, y, input_num):
    color = paper[x][y]
    for i in range(x, x+input_num):
        for j in range(y, y+input_num):
            if color != paper[i][j]:
                solution(x, y, input_num//2)
                solution(x, y+input_num//2, input_num//2)
                solution(x+input_num//2, y, input_num//2)
                solution(x+input_num//2, y+input_num//2, input_num//2)
                return

    if color == 0:    #흰색일때 0으로 설정
        result.append(0)
    else:
        result.append(1)

solution(0, 0, input_num)
print(result.count(0))
print(result.count(1))