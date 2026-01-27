import sys
from collections import Counter

x_list = []
y_list = []

for i in range(3):
    a, b = map(int,sys.stdin.readline().strip().split())

    x_list.append(a)
    y_list.append(b)

x_counter = Counter(x_list)
y_counter = Counter(y_list)

x_ans = min(x_counter, key=x_counter.get)
y_ans = min(y_counter, key=y_counter.get)

print(f"{x_ans} {y_ans}")