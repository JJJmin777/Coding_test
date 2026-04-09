import sys
from collections import deque

n = int(sys.stdin.readline().strip())

num_q = deque([i for i in range(1, n + 1)])
ballon_q = deque(list(map(int, sys.stdin.readline().strip().split())))

an_list = []

x = ballon_q.popleft()
an_list.append(num_q.popleft())

while len(ballon_q) > 0:
    if x > 0:
        for _ in range(x - 1):
            if ballon_q:
                ballon_q.append(ballon_q.popleft())
            if num_q:
                num_q.append(num_q.popleft())
    else:
        for _ in range(-x):
            if ballon_q:
                ballon_q.appendleft(ballon_q.pop())
            if num_q:  
                num_q.appendleft(num_q.pop())

    x = ballon_q.popleft()
    an_list.append(num_q.popleft())

print(" ".join(map(str, an_list)))