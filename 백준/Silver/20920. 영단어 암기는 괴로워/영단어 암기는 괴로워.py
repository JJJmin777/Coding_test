import sys
from collections import Counter

N, M = map(int, sys.stdin.readline().strip().split())

s_list = []
s_set = set()

for _ in range(N):
    s = sys.stdin.readline().strip()

    if len(s) >= M:
        s_list.append(s)

cnt = Counter(s_list)

sorted_count = sorted(cnt.items(), key= lambda x : (-x[1], -len(x[0]), x[0]))

for i in range(len(sorted_count)):
    print(sorted_count[i][0])