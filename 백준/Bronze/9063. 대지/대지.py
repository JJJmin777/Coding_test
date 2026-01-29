import sys


num = int(sys.stdin.readline().strip())

x_list = []
y_list = []

for _ in range(num):
    a, b = map(int, sys.stdin.readline().strip().split())

    x_list.append(a)
    y_list.append(b)

x_len = max(x_list) - min(x_list)
y_len = max(y_list) - min(y_list)

print(x_len * y_len)