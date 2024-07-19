import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = [input().rstrip() for _ in range(n)]
results = []

for i in range(n-7):
    for j in range(m-7):
        b_start = 0
        w_start = 0
        for x in range(i,i+8):
            for y in range(j, j+8):
                if (x+y)%2 == 0:
                    if board[x][y] != 'B':
                        b_start += 1
                    else:
                        w_start += 1
                else:
                    if board[x][y] != 'B':
                        w_start += 1
                    else:
                        b_start += 1
        results.append(b_start)
        results.append(w_start)

print(min(results))