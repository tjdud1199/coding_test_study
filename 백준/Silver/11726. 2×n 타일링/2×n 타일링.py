import sys

input = sys.stdin.readline

n = int(input().rstrip())

dp = [0,1,2,3]

if n > 3:
    for i in range(4, n+1):
        dp.append(dp[i-1]+dp[i-2])

print(dp[n]%10007)