import sys

input = sys.stdin.readline

# 키, 몸무게 (x,y)
# 덩치 등수 : 더 큰 덩치 사람 수 k + 1

n = int(input().rstrip())
info = []
scores = [1 for i in range(n)]

for _ in range(n):
    x, y = map(int, input().split())
    info.append([x,y])

for i in range(n):
    x, y = info[i]
    for j in range(n):
        p, q = info[j]
        if x < p and y < q:
            scores[i] += 1

print(*scores)