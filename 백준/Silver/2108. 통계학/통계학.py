import sys
import math

input = sys.stdin.readline

n = int(input().rstrip())
nums = [int(input().rstrip()) for _ in range(n)]
nums.sort()

dic = {}
for num in nums:
    dic[num] = dic.get(num, 0) + 1

d_max = max(dic.values())
most = []
for k, v in dic.items():
    if v == d_max:
        most.append(k)
most.sort()

print(math.floor(sum(nums)/n+0.5))
print(nums[int(n//2)])

if len(most) == 1:
    print(most[0])
else:
    print(most[1])
    
print(abs(nums[-1]-nums[0]))