t = int(input())

for i in range(1,t+1):
    p, q, r, s, w = map(int, input().split())
    a = w*p
    if w <= r:
        b = q
    else:
        b = q + (w-r)*s
    print('#'+str(i), min(a, b))