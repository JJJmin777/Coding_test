import sys

N, K = map(int, sys.stdin.readline().strip().split())

n = 1
k = 1

for i in range(N , N - K, -1):
    n *= i

for i in range(1, K + 1):
    k *= i

print(int(n / k))