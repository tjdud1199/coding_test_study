t = int(input())

for i in range(1, t+1):
    nums = list(map(int, input().split()))
    res = 0
    rm = [min(nums), max(nums)]
    for num in nums:
        if num not in rm:
            res += num
    print('#'+str(i), round(res/(len(nums)-2)))