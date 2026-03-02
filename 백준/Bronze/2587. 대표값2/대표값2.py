import sys

num_list = [int(sys.stdin.readline()) for _ in range(5)]


average = int(sum(num_list) / 5)

num_list = sorted(num_list)
print(average)
print(num_list[2])