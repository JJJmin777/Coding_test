import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))

target = 1
stack = []


for x in arr:
    while stack and stack[-1] == target:
        stack.pop()
        target += 1
    
    if x == target:
        target += 1
    else:
        stack.append(x)

while stack and stack[-1] == target:
    stack.pop()
    target += 1

print("Nice" if target == n + 1 else "Sad")