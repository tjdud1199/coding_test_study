import sys

input = sys.stdin.readline

n = int(input().rstrip())
nums = [0 for _ in range(10001)]

for _ in range(n):
    num = int(input().rstrip())
    nums[num] += 1

for i in range(1, 10001):
    num = nums[i]
    if num != 0:
        for j in range(num):
            print(i)
