t = int(input())

for i in range(1, t+1):
    case = input()
    madi = ''
    for j in range(30):
        madi += case[j]
        if madi == str(case[j+1:j+len(madi)+1]):
            print('#'+str(i), len(madi))
            break