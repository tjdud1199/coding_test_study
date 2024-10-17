t = int(input())

for i in range(1, t+1):
    nums = [i for i in list(map(int, input().split())) if i%2==1]
    print('#'+str(i), sum(nums))