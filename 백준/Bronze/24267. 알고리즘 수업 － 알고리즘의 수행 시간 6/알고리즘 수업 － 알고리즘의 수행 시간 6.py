import sys

n = int(sys.stdin.readline().strip())
sum = 0

for i in range(1, n - 1):
    a = int(i * (i + 1) / 2)
    sum += a

print(sum)
print(3)