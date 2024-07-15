import sys

input = sys.stdin.readline

n = int(input().rstrip())
nums = [list(map(int,input().split())) for _ in range(n)]
nums.sort(key=lambda x: (int(x[1]), int(x[0])))

for num in nums:
    print(*num)