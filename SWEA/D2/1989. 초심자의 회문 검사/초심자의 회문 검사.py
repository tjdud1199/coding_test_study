t = int(input())

for i in range(1, t+1):
    word = input()
    mid = len(word)//2
    if len(word)%2 == 1:
        if word[:mid+1] == word[-1:mid-1:-1]:
            res = 1
        else:
            res = 0
    else:
        if word[:mid] == word[-1:mid-1:-1]:
            res = 1
        else:
            res = 0
    print('#'+str(i), res)
