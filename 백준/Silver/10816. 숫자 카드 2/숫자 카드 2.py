import sys

card_num = int(sys.stdin.readline().strip())

count_dict = {}
ans_list = []

nums = map(int, sys.stdin.readline().strip().split())

for n in nums:
    # if n in count_dict:
    #     count_dict[n] += 1
    # else:
    #     count_dict[n] = 1
    count_dict[n] = count_dict.get(n, 0) + 1

ans_num = int(sys.stdin.readline().strip())
s = list(map(int, sys.stdin.readline().strip().split()))

for num in s:
    ans_list.append(count_dict.get(num, 0))

print(*ans_list)
