import sys
from collections import deque

N = int(sys.stdin.readline().strip())

q = deque()

for _ in range(N):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "push":
        q.append(int(cmd[1]))
    elif cmd[0] == "pop":
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(q))
    elif cmd[0] == "empty":
        if not q:
            print(1)
        else:
            print(0)
    elif cmd[0] == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    elif cmd[0] == "back":
        if q:
            print(q[-1])
        else:
            print(-1)
