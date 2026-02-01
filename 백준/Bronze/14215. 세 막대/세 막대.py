import sys

num_list = list(map(int, sys.stdin.readline().strip().split()))

while True:
    if max(num_list) < (sum(num_list) - max(num_list)):
        print(sum(num_list))
        break
    else:
        idx = num_list.index(max(num_list))
        num_list[idx] -= 1