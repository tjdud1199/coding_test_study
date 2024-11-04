t = int(input())

for i in range(1, t+1):
    n = int(input())
    res = sum([j for j in range(1,n+1,2)]) - sum([j for j in range(0,n+1,2)])
    print('#'+str(i), res)