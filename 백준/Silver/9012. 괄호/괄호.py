import sys

n = int(sys.stdin.readline().strip())

for _ in range(n):
    str = sys.stdin.readline().strip()
    stack = []
    sol = True

    for s in str:
        if s == "(":
            stack.append(s)
        elif s == ")":
            if stack:
                stack.pop()
            else:
                print("NO")
                sol = False
                break
    if sol:
        if stack:
            print("NO")
        else:
            print("YES")
                    