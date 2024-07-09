import sys

input = sys.stdin.readline

while True:
    nums = list(map(int, input().split()))
    nums.sort()
    if nums[0] == 0:
        break
    if nums[0]**2 + nums[1]**2 == nums[2]**2:
        print('right')
    else:
        print('wrong')