import sys

def gcd(a, b):
    while b != 0:
        a , b = b , a % b
    return a

a, b = map(int, sys.stdin.readline().strip().split())
c, d = map(int, sys.stdin.readline().strip().split())

ans_2 = (b*d) // gcd(b, d)

ans_1 = (a*(ans_2 // b)) + (c*(ans_2 // d))

if gcd(ans_1, ans_2) == 1:
    print(ans_1, ans_2)
else:
    x = gcd(ans_1, ans_2)
    print(ans_1 // x, ans_2 // x)
