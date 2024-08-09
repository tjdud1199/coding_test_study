import sys

input = sys.stdin.readline

n = int(input().rstrip())
dp = [0 for _ in range(n+1)]

if n == 1:
    print(0)
elif n == 2 or n == 3:
    print(1)
else:
    dp[2], dp[3] = 1, 1
    for i in range(4,n+1):
        if i % 3 == 0 and i % 2 == 0:
            dp[i] = min(dp[i//3], dp[i//2], dp[i-1]) + 1
        elif i % 3 == 0:
            dp[i] = min(dp[i//3], dp[i-1]) + 1
        elif i % 2 == 0:
            dp[i] = min(dp[i//2], dp[i-1]) + 1
        else:
            dp[i] = dp[i-1] + 1
    
    print(dp[n])