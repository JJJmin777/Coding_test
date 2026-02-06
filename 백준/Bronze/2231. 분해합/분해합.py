import sys

num = int(sys.stdin.readline().strip())

ans_list = []

for i in range(10):
    for j in range(10):
        for k in range(10):
            for m in range(10):
                for l in range(10):
                    for n in range(10):
                        for o in range(10):
                            if num == (i*1000000 + j*100000 + k*10000 + m*1000 + l*100 + n*10 + o + i + j + k + m + l + n + o):
                                ans = i*1000000 + j*100000 + k*10000 + m*1000 + l*100 + n*10 + o
                                ans_list.append(ans)

if len(ans_list) == 0:
    print(0)
else:
    print(min(ans_list))