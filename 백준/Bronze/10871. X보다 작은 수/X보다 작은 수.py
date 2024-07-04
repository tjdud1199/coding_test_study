import sys

input = sys.stdin.readline

n, x = map(int, input().split())
nums = [i for i in map(int, input().split())]
result = []

for num in nums:
    if num < x:
        result.append(num)

print(*result)