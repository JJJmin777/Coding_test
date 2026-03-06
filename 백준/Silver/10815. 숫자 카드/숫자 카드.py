import sys

to_list = [0 for i in range(20000000)] 
ans_list = []

card_num = int(sys.stdin.readline().strip())

card_list = list(map(int, sys.stdin.readline().strip().split()))

for i in card_list:
    to_list[i] = 1

n = int(sys.stdin.readline().strip())

s = list(map(int, sys.stdin.readline().strip().split()))

for i in s:
    if to_list[i] == 1:
        ans_list.append(1)
    else:
        ans_list.append(0)

print(*ans_list)