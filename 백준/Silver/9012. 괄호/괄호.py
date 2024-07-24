import sys

input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    ps = input().rstrip()
    result = 'YES'
    check = 0
    for p in ps:
        if p == '(':
            check += 1
        else:
            check -= 1
            if check < 0:
                result = 'NO'
                break
    if check != 0:
        result = 'NO'
        
    print(result)

