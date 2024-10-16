t = int(input())
for i in range(1, t+1):
    a, b = map(int, input().split())
    if a > b:
        res = '>'
    elif a == b:
        res = '='
    else:
        res = '<'
    print('#'+str(i), res)