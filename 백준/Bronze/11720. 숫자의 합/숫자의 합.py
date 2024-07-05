
import sys

input = sys.stdin.readline

n = int(input().rstrip())
nums = input().rstrip()
result = 0

for num in nums:
    result += int(num)

print(result)