import sys

def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n-1)
    
x = int(sys.stdin.readline().strip())

print(1 if x == 0 else fac(x))
