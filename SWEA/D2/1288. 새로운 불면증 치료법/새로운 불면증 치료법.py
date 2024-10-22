t = int(input())

for i in range(1, t+1):
    n = int(input())
    ans = set([i for i in range(10)])
    res = set()
    k = 0
    while True:
        k += 1
        kn = str(k * n)
        for j in kn:
            res.add(int(j))
        if res == ans:
            print('#'+str(i), kn)
            break