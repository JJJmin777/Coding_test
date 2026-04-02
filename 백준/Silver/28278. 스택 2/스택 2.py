import sys

n = int(sys.stdin.readline().strip())
stack = []

for _ in range(n):
    line = sys.stdin.readline().strip().split()

    if len(line) == 2:
        a, b = map(int, line)
        stack.append(b)

    else:
        b = int(line[0])

        if b == 2:
            if stack:
                print(stack.pop())
            else:
                print(-1)

        elif b == 3:
            print(len(stack))

        elif b == 4:
            if stack:
                print(0)
            else:
                print(1)

        elif b == 5:
            if stack:
                print(stack[-1])
            else:
                print(-1)
