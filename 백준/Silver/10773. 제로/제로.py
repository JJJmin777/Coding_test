import sys

n = int(sys.stdin.readline().strip())

stack = []

for _ in range(n):
    a = int(sys.stdin.readline().strip())

    if a == 0:
        stack.pop()

    else:
        stack.append(a)

print(sum(stack))