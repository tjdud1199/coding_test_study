import sys

input = sys.stdin.readline

n = int(input().rstrip())
dp = [-1 for _ in range(n+1)]

dp[3] = 1

if n >= 5:
	dp[5] = 1

for i in range(6,n+1):
    comp = []
    if dp[i-3] != -1:
        comp.append(dp[i-3]+1)
    if i >= 5:
        if dp[i-5] != -1:
            comp.append(dp[i-5]+1)
    if comp:
        dp[i] = min(comp)

print(dp[n])