import sys

input = sys.stdin.readline
nums = []

for _ in range(10):
    num = int(input().rstrip())
    nums.append(num%42)

print(len(set(nums)))