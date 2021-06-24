import sys

while True:
    string = sys.stdin.readline().rstrip()

    if string == '.':
        break

    array = []

    judgment = True
    for i in string:
        if i == '(' or i == '[':
            array.append(i)
        elif i == ')':
            if len(array) > 0 and array[-1] == '(':
                array.pop()
            else:
                judgment = False    # 스택이 비어있는데 ')' 가 나온 경우
        elif i == ']':
            if len(array) > 0 and array[-1] == '[':
                array.pop()
            else:
                judgment = False   # 스택이 비어있는데 ']' 가 나온 경우

    if len(array) == 0 and judgment == True:
        print('yes')
    else:
        print('no')