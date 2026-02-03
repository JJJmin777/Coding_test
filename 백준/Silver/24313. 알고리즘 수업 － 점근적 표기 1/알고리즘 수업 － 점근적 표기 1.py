import sys

a1, a0 = map(int, sys.stdin.readline().strip().split())
c = int(sys.stdin.readline().strip())
n0 = int(sys.stdin.readline().strip())

print(1 if a1*n0 + a0 <= c*n0 and a1 <= c else 0)