import sys

num, award = map(int, sys.stdin.readline().strip().split())

num_list = list(map(int, sys.stdin.readline().strip().split()))


num_list = sorted(num_list, reverse=True)

print(num_list[award - 1])