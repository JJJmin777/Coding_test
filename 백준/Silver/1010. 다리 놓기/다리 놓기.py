import sys

T = int(sys.stdin.readline().strip())


for _ in range(T):
    
    n = 1
    k = 1
    N, M = map(int, sys.stdin.readline().strip().split())

    for i in range(M , M - N, -1):
        n *= i

    for i in range(1,N + 1):
        k *= i  

    print(int(n / k))