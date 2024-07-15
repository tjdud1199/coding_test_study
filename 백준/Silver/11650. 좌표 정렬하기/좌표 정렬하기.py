import sys

input = sys.stdin.readline

n = int(input().rstrip())
nums = [list(map(int, input().split())) for _ in range(n)]
nums.sort(key = lambda x: (x[0], x[1]))

for num in nums:
    print(*num)