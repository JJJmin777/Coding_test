import sys

num = int(sys.stdin.readline().strip())

member_list = [sys.stdin.readline().strip().split() for i in range(num)]

member_list.sort(key= lambda x: int(x[0]))

for x , y in member_list:
    print(x , y)