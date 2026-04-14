import sys
import math
from collections import Counter

N = int(sys.stdin.readline().strip())

num_list = [int(sys.stdin.readline().strip()) for _ in range(N)]
num_list.sort()

print(math.floor((sum(num_list) / N) + 0.5))

print(num_list[N // 2])

cnt = Counter(num_list)

max_count = max(cnt.values())

result = [k for k, v in cnt.items() if v == max_count]

if len(result) == 1:
    print(result[0])
else:
    print(result[1])

print(num_list[-1] - num_list[0])
