t = int(input())

for i in range(1, t+1):
    n = int(input())
    prices = list(reversed(list(map(int, input().split()))))
    price = prices[0]
    buy = 0
    sell = 0
    
    for j in prices[1:]:
        if j < price:
            sell += price
            buy += j
        else:
            price = j
    print('#'+str(i), sell-buy)