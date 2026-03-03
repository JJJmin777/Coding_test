import sys

num = int(sys.stdin.readline().strip())

count_list = [0 for i in range(10001)]


for i in range(num):
    N = int(sys.stdin.readline().strip())
    count_list[N] += 1

for i in range(10001):
    for _ in range(count_list[i]):
        print(i)