import sys

input = sys.stdin.readline

n = int(input().rstrip())
dp = [-1 for _ in range(n)]

for i in range(3,n+1):
    comp = []
    idx = i-1
    if i == 3:
        dp[idx] = 1
    elif i == 5:
        dp[idx] = 1
    else:
        if dp[idx-3] != -1:
            comp.append(dp[idx-3]+1)
        if i >= 5:
            if dp[idx-5] != -1:
                comp.append(dp[idx-5]+1)
    if comp:
        dp[idx] = min(comp)

print(dp[n-1])