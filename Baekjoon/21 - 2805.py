tree_num, wood = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 0, max(trees)
current_guess = (start + end) // 2


while start <= end:

    if wood == 1:
        print(max(trees)-1)
        break

    sum = 0
    for tree in trees:
        if tree >= current_guess:
            sum += tree - current_guess

    if sum >= wood:  # 가장 헷갈리는 부분. 적어도 나무를 자른 총량이 wood 이상이어야 된다. sum이 wood와 딱 맞아떨이지지 않는 경우가 생긴다.
        # 말은 이해되는데 정확히 어떻게 이렇게 이진탐색으로 탐색이 되는지 모르겠다.
        start = current_guess + 1
        # print("start: " + str(start))
    else:
        end = current_guess - 1
        # print("end: " + str(end))

    current_guess = (start + end) // 2

print(current_guess) # 처음에 무조건 sum == tree_length와 같아지는 경우가 나올꺼라 생각했으나 아니였음. start <= end 조건을 빠져나오면
                        # 바로 출력해주어야 함