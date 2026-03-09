import sys


str_num, ans_num= map(int, sys.stdin.readline().strip().split())


count = 0


str_list = [sys.stdin.readline().strip() for _ in range(str_num)]
str_set = set(str_list)


s = [sys.stdin.readline().strip() for _ in range(ans_num)]

for i in range(len(s)):
    if s[i] in str_set:
        count += 1

print(count)