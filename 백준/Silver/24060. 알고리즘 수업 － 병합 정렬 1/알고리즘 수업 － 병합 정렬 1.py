import sys
                      
N, K = map(int, sys.stdin.readline().strip().split())

input_list = list(map(int, sys.stdin.readline().strip().split()))

count = 0
answer = -1

def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    global count, answer

    i = p
    j = q + 1
    tmp = []

    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1
    
    while i <= q:
        tmp.append(A[i])
        i += 1

    while j <= r:
        tmp.append(A[j])
        j += 1

    i = p
    for x in tmp:
        A[i] = x
        count += 1

        if count == K:
            answer = x
        
        i += 1

merge_sort(input_list, 0, N - 1)

print(answer)
    