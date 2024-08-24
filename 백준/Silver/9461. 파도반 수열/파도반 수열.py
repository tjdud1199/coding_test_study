import sys

input = sys.stdin.readline

dp = [0,1,1,1,2,2,3,4,5,7,9]

for _ in range(int(input().rstrip())):
    n = int(input().rstrip())
    if n > 10:
        for _ in range(11, n+1):
            dp.append(dp[-5]+dp[-1])
    print(dp[n])