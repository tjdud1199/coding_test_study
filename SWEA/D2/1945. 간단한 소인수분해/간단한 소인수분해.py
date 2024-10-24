t = int(input())

for i in range(1, t+1):
    n = int(input())
    nums = [2,3,5,7,11]
    res = [0,0,0,0,0]
    for j in range(5):
        while True:
            if n % nums[j] == 0:
                res[j] += 1
                n //= nums[j]
            else:
                break
    print('#'+str(i),*res, sep=' ')