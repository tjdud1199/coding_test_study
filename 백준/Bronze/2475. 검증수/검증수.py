import sys

input = sys.stdin.readline

nums = [i**2 for i in map(int, input().split())]

print(sum(nums)%10)