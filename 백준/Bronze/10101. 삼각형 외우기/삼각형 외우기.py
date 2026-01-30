import sys

an_list = []

for _ in range(3):
    input = int(sys.stdin.readline().strip())
    an_list.append(input)

if an_list[0] == 60 and an_list[1] == 60 and an_list[2] == 60:
    print("Equilateral")
else:
    if sum(an_list) == 180:
        if an_list[0] == an_list[1] or an_list[0] == an_list[2] or an_list[1] == an_list[2]:
            print("Isosceles")
        else:
            print("Scalene")

    else:
        print("Error")