import sys


num = int(sys.stdin.readline().strip())

s = list(map(int, sys.stdin.readline().strip().split()))

sorted_list = sorted(list(set(s)))

comp = {v:i for i, v in enumerate(sorted_list)}

print(*(comp[x] for x in s))