t = int(input())

for i in range(1, t+1):
    n = int(input())
    res = ''
    for _ in range(n):
        alpha, x = input().split()
        res += alpha * int(x)
    print('#'+str(i))
    while True:
        if len(res) > 10:
            print(res[:10])
            res = res[10:]
        else:
            print(res[:])
            break