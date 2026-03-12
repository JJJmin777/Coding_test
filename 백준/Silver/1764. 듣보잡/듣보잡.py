import sys

N, M = map(int, sys.stdin.readline().strip().split())

n_set = set([sys.stdin.readline().strip() for _ in range(N)])
m_set = set([sys.stdin.readline().strip() for _ in range(M)])

answer = n_set & m_set

print(len(answer))
for i in sorted(answer):
    print(i)