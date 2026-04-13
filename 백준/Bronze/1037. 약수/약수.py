import sys

N = int(sys.stdin.readline().strip())

a_list = list(map(int, sys.stdin.readline().strip().split()))
a_list.sort()

if N % 2 == 1:
    x = (N // 2)
    print(a_list[x]**2)
else:
    print(a_list[0] * a_list[-1])