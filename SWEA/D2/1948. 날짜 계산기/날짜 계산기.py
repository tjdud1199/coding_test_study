t = int(input())

for i in range(1, t+1):
    m1, d1, m2, d2 = map(int, input().split())
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    td1 = sum(days[:m1-1]) + d1
    td2 = sum(days[:m2-1]) + d2
    print('#'+str(i),td2 - td1 + 1)