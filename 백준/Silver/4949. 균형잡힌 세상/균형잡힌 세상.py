import sys

while True:
    s = sys.stdin.readline().rstrip()
    stack = []

    if s == ".":
        break
    else:
        for ch in s:
            if ch == "(":
                stack.append(ch)
            elif ch == "[":
                stack.append(ch)
            elif ch == ")":
                if stack:
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        print("no")
                        break
                else:
                    print("no")
                    break
            elif ch == "]":
                if stack:
                    if stack[-1] == "[":
                        stack.pop()
                    else:
                        print("no")
                        break
                else:
                    print("no")
                    break
        
        else:
            if stack:
                print("no")
            else:
                print("yes")