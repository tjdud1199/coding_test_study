import sys

input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    k = int(input().rstrip())
    n = int(input().rstrip())
    rooms = [[i+1 for i in range(n)] for _ in range(k+1)]
    for i in range(1,k+1):
        for j in range(n):
            if j == 0:
                rooms[i][j] = 1
            else:
                rooms[i][j] = rooms[i][j-1] + rooms[i-1][j]
    print(rooms[k][n-1])