import sys

N = int(sys.stdin.readline().strip())

name_set = set()

name_set.add("ChongChong")

for _ in range(N):
    name1, name2 = map(str, sys.stdin.readline().strip().split())

    if name1 in name_set or name2 in name_set:
        name_set.add(name1)
        name_set.add(name2)

print(len(name_set))