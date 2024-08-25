import sys

input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))
prefix_sum = [0]

for i in nums:
    prefix_sum.append(prefix_sum[-1]+i)

for _ in range(m):
    s, e = map(int, input().split())
    result = prefix_sum[e] - prefix_sum[s-1]
    print(result)