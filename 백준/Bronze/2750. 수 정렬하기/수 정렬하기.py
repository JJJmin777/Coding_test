import sys

num = int(sys.stdin.readline().strip())
arr = []

for i in range(num):
    arr.append(int(sys.stdin.readline().strip()))

new_arr = sorted(arr)

for i in (new_arr):
    print(i)