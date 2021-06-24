num = int(input())
count = 0

for i in range(0, num):
    word = input()

    groupword = True
    for j in range(0, len(word)):
        if word.count(word[j]) < 2:
            continue

        duplication_index = []
        find_index = word.find(word[j])
        duplication_index.append(find_index)
        while word[find_index + 1:].find(word[j]) != -1:
            find_index = word[find_index + 1:].find(word[j]) + find_index + 1
            duplication_index.append(find_index)

        for k in range(0,len(duplication_index)-1):
            if duplication_index[k+1] != duplication_index[k] + 1:
                groupword = False

    if groupword == True:
        count += 1

print(count)