import sys

num = sys.stdin.readline().strip()

num_list = [int(i) for i in num]

sorted_list = sorted(num_list, reverse=True)

print(''.join(map(str, sorted_list)))