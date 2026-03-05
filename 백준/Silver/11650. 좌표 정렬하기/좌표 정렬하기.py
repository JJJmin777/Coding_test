import sys

num = int(sys.stdin.readline().strip())

xy_list = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(num)]

xy_list.sort()

for x, y in xy_list:
    print(x, y)