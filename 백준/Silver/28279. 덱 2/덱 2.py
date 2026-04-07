import sys
from collections import deque

n = int(sys.stdin.readline().strip())
q = deque()
out = []

for _ in range(n):
    cmd = sys.stdin.readline().split()

    if cmd[0] == "1":
        q.appendleft(cmd[1])
    elif cmd[0] == "2":
        q.append(cmd[1])
    elif cmd[0] == "3":
        out.append(q.popleft() if q else -1)
    elif cmd[0] == "4":
        out.append(q.pop() if q else -1)
    elif cmd[0] == "5":
        out.append(len(q))
    elif cmd[0] == "6":
        out.append(0 if q else 1)
    elif cmd[0] == "7":
        out.append(q[0] if q else -1)
    elif cmd[0] == "8":
        out.append(q[-1] if q else -1)

sys.stdout.write("\n".join(map(str, out)))