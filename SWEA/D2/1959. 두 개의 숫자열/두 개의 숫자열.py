t = int(input())

for i in range(1, t+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    res = []
    
    if n > m:
        aj = b
        bj = a
        n, m = m, n
    else:
        aj = a
        bj = b
    
    for j in range(m-n+1):
        cal = sum([aj[q]*bj[j+q] for q in range(n)])
        res.append(cal)
    
    print('#'+str(i), max(res))