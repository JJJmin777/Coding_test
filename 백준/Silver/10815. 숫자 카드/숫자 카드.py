import sys

result = []

card_num = int(sys.stdin.readline().strip())

card_list = list(map(int, sys.stdin.readline().strip().split()))
card_set = set(card_list)

n = int(sys.stdin.readline().strip())

s = list(map(int, sys.stdin.readline().strip().split()))

print(*(1 if x in card_set else 0 for x in s))