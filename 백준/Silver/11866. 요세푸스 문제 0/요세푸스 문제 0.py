import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

an_list = []
q = deque()

for i in range(1, n + 1):
    q.append(i)

while len(q) > 0:
    for _ in range(k - 1):
        q.append(q.popleft())

    an_list.append(q.popleft())

print("<" + ", ".join(map(str, an_list)) + ">")