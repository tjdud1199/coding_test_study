import sys

input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    n = int(input().rstrip())
    dp = [0,1,2,4]
    if n > 3:
        for i in range(4,n+1):
            dp.append(dp[i-1] + dp[i-2] + dp[i-3])
    print(dp[n])