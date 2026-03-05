import sys

num = int(sys.stdin.readline().strip())

str_list = [sys.stdin.readline().strip() for _ in range(num)]

re_list = list(set(str_list))

re_list.sort(key= lambda x : (len(x), x))


for i in re_list:
    print(i)