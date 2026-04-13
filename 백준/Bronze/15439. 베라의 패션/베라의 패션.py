import sys

n = int(sys.stdin.readline().strip())

if n == 1:
    print(0)
else:
    print(n*(n-1))