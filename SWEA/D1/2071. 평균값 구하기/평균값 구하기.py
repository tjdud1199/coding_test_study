import math
t = int(input())
for i in range(1, t+1):
    nums = list(map(int, input().split()))
    res = math.floor((sum(nums))/10+0.5)
    print('#'+str(i),res)