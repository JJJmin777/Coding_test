import sys

a_num, b_num = map(int, sys.stdin.readline().strip().split())

a_set = set(sys.stdin.readline().strip().split())
b_set = set(sys.stdin.readline().strip().split())

ans_set = (a_set - b_set) | (b_set - a_set)

print(len(ans_set))