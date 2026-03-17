import sys

n = int(sys.stdin.readline().strip())

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a



for i in range(n):
    a, b = map(int, sys.stdin.readline().strip().split())
    print((a*b) // gcd(a, b))