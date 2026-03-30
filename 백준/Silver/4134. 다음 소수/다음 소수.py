import sys

n = int(sys.stdin.readline().strip())

def is_prime(x):
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

for i in range(n):
    x = int(sys.stdin.readline().strip())

    if x <= 2:
        print(2)
    else:    
        while True:
            if is_prime(x):
                print(x)
                break
            else:
                x += 1
            