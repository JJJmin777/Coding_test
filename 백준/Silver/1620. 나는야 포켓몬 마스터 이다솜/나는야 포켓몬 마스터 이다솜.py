import sys

num, ans_num = map(int, sys.stdin.readline().strip().split())

name_to_num = {}
num_to_name = {}

for i in range(1, num + 1):
    name = sys.stdin.readline().strip()
    name_to_num[name] = i
    num_to_name[i] = name

for i in range(ans_num):
    a = sys.stdin.readline().strip()
    if a.isdigit():
        print(num_to_name[int(a)])
    else:
        print(name_to_num[a])