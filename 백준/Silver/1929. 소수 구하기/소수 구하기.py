import sys
import math

input = sys.stdin.readline

m, n = map(int, input().split())

nums = [True]*(n+1)

for i in range(2, int(math.sqrt(n))+1):
    if nums[i]:
        for j in range(i*i, n+1, i):
            nums[j] = False

for i in range(max(2,m), n+1):
    if nums[i]:
        print(i)