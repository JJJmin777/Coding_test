import sys


num = int(sys.stdin.readline().strip())
answer_set = set()

for i in range(num):
    name, a = map(str, sys.stdin.readline().strip().split())

    if a == "enter":
        answer_set.add(name)
    elif a == "leave":
        answer_set.remove(name)

for i in sorted(answer_set, reverse=True):
    print(i)
