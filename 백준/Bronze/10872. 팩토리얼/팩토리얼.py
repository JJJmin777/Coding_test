import sys

n = int(sys.stdin.readline().strip())

ans = 1

if n == 0:
    print(ans)
else:
    for i in range(1, n + 1):
        ans *= i
    print(ans)
