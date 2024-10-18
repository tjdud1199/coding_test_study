T = int(input())

for _ in range(T):
    t = int(input())
    nums = [0 for i in range(101)]
    case = list(map(int, input().split()))
    for num in case:
        nums[num] += 1
    keys = []
    max_value = max(nums)
    for i, cnt in enumerate(nums):
        if cnt == max_value:
            keys.append(i)
    print('#'+str(t),max(keys))