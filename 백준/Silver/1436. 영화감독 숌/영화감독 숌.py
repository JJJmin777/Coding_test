import sys

num = int(sys.stdin.readline().strip())

count = 0
n = 0

while True:
    if "666" in str(n):
        count += 1
        if count == num:
            print(n)
            break
    n += 1
