import sys

n = int(sys.stdin.readline().strip())
count = 0
namues = []

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

for _ in range(n):
    namues.append(int(sys.stdin.readline().strip()))
    
diffs = [namues[i + 1] - namues[i] for i in range(len(namues) - 1)]

g = diffs[0]

for i in range(1, len(diffs)):
    g = gcd(g, diffs[i])
    
for i in range(len(diffs)):
    count += (diffs[i] // g) - 1
    
print(count)
    
    