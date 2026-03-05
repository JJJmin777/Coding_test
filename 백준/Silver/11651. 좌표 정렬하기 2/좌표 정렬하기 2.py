import sys

num = int(sys.stdin.readline().strip())

xy_list = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(num)]

xy_list.sort(key= lambda x: (x[1], x[0]))

for x, y in xy_list:
    print(x, y)        