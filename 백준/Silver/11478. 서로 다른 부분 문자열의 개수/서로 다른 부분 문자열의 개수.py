import sys

str = sys.stdin.readline().strip()
an_list = []

for i in range(len(str)):
    for j in range(i + 1, len(str) + 1):
        an_list.append(str[i:j])
        # print(str[i:j])

ans_set = set(an_list)

print(len(ans_set))