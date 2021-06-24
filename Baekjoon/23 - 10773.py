import sys

line = int(sys.stdin.readline().rstrip())
num_stack = []
for _ in range(line):
    num = int(sys.stdin.readline().rstrip())

    if num != 0:
        num_stack.append(num)
    else:
        num_stack.pop()

print(sum(num_stack))
