import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input().rstrip()) for _ in range(n)]
result = 0

for coin in reversed(coins):
    cnt = k // coin
    result += cnt
    k -= coin * cnt
    if k == 0:
        break

print(result)