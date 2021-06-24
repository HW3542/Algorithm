N, M = map(int, input().split())

check_list = [False] * N
output = []

def dfs(depth, N, M):
    if depth == M:
        print(' '.join([str(x) for x in output]))
        return
    for i in range(N):
        if check_list[i]:
            continue
        check_list[i] = True
        output.append(i+1)
        dfs(depth+1, N, M)
        output.pop()
        for j in range(i+1, N):
            check_list[j] = False

dfs(0, N, M)