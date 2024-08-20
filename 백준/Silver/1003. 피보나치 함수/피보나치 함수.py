import sys

input = sys.stdin.readline

dp_0 = [1,0,1,1]
dp_1 = [0,1,1,2]

for _ in range(int(input().rstrip())):
    n = int(input().rstrip())
    if n < 4:
        print(dp_0[n], dp_1[n])
    else:
        for i in range(4, n+1):
            dp_0.append(dp_0[-1] + dp_0[-2])
            dp_1.append(dp_1[-1] + dp_1[-2])
        print(dp_0[n], dp_1[n])