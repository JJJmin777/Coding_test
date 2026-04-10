import sys
from collections import deque

an_list = []

n = int(sys.stdin.readline().strip())

A_list = list(map(int, sys.stdin.readline().strip().split()))

B_list = list(map(int, sys.stdin.readline().strip().split()))

m = int(sys.stdin.readline().strip())

C_list = list(map(int, sys.stdin.readline().strip().split()))

q = deque()

for i in range(n-1, -1, -1):
    if A_list[i] == 0:
        q.append(B_list[i])

for x in C_list:
    q.append(x)

for i in range(m):
    an_list.append(str(q.popleft()))


print(" ".join(an_list))