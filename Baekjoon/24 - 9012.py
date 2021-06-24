import sys

line = int(input())


def search_parenthesis(string):
    array = []

    for i in string:
        if i == '(':
            array.append(1)
        else:
            if len(array) == 0:
                return print('NO')
            array.pop()

    if len(array) == 0:
        print('YES')
    else:
        print('NO')

for _ in range(line):
    string = sys.stdin.readline().rstrip()

    search_parenthesis(string)
