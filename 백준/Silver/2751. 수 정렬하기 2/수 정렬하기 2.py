import sys

num = int(sys.stdin.readline().strip())

num_list = [int(sys.stdin.readline().strip()) for _ in range(num)]


num_list = sorted(num_list)

for i in range(len(num_list)):
    print(num_list[i])