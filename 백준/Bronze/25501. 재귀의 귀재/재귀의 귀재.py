import sys

def recursion(s, l, r):
    global recursion_count
    recursion_count += 1
    if l >= r: return 1
    elif s[l] != s[r] : return 0
    else:
        return recursion(s, l + 1, r - 1)

def isPalindrome(s):
    global recursion_count
    recursion_count = 0

    result = recursion(s, 0, len(s)-1)
    return result, recursion_count


T = int(sys.stdin.readline().strip())

for _ in range(T):
    s = sys.stdin.readline().strip()

    a = isPalindrome(s)
    print(a[0], a[1])