import sys

n = int(sys.stdin.readline().strip())

arr = []

for _ in range(n):
    arr.append(int(sys.stdin.readline().strip()))

max_x = max(arr)

prime = [True] * (max_x + 1)
    
prime[0] =prime[1] = False

for i in range(2, int(max_x**0.5) + 1):
    if prime[i]:
        for j in range(i*i, max_x + 1, i):
            prime[j] = False

for x in arr:
    count = 0

    for a in range(2, x//2 + 1):
        if prime[a] and prime[x - a]:
            count += 1

    print(count)