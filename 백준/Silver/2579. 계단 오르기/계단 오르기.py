import sys

input = sys.stdin.readline

n = int(input().rstrip())
scores = [0 for _ in range(301)]

for i in range(1,n+1):
    scores[i] = int(input().rstrip())

dp = [0 for _ in range(301)]
dp[1] = scores[1]
dp[2] = scores[1] + scores[2]
dp[3] = max(scores[1]+scores[3], scores[2]+scores[3])

if n > 3:
    for i in range(4, n+1):
        dp[i] = max(dp[i-3]+scores[i-1]+scores[i], dp[i-2]+scores[i])

print(dp[n])