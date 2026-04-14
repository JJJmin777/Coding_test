import sys

N = int(sys.stdin.readline().strip())

name_set = set()
ans = 0

for _ in range(N):
    name = sys.stdin.readline().strip()
    
    if name == "ENTER":
        ans += len(name_set)
        name_set = set()
    else:
        name_set.add(name)

ans += len(name_set)

print(ans)