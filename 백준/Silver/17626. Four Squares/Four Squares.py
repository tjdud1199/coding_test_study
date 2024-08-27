import sys
import math

input = sys.stdin.readline

n = int(input().rstrip())

dp = [float('inf')] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    j = 1
    while j * j <= i:
        dp[i] = min(dp[i], dp[i - j * j] + 1)
        j += 1

print(dp[n])