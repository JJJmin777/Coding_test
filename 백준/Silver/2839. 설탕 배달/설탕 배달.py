import sys

num = int(sys.stdin.readline().strip())
ans_list = []

target = num // 5

for i in range(target, -1, -1):
    if i == 0:
        a = num
    else:
        a = num - (5*i)
    
    if a % 3 == 0:
        j = int(a / 3)
        ans_list.append(i + j)

if not ans_list:
    print(-1)
else:
    print(min(ans_list))