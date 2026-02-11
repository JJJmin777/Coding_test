import sys

n, m = map(int, sys.stdin.readline().strip().split())

board = [sys.stdin.readline().strip() for _ in range(n)]

answer = 64

for i in range(n - 7):
    for j in range(m -7):
        repaint_w = 0
        repaint_b = 0

        for x in range(8):
            for y in range(8):
                cur = board[i + x][j + y]

                expected_w = "W" if (x + y) % 2 == 0 else "B"
                expected_b = "B" if (x + y) % 2 == 0 else "W"

                if cur != expected_w:
                    repaint_w += 1
                if cur != expected_b:
                    repaint_b += 1
                
        answer = min(answer, repaint_b, repaint_w)
        
print(answer)