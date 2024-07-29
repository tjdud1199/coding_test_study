import sys

input = sys.stdin.readline
now = 1
sign = []
stack = []
temp = True

for _ in range(int(input().rstrip())):
    num = int(input().rstrip())
    while now <= num:
        stack.append(now)
        sign.append('+')
        now += 1
    
    check = stack.pop()
    if check == num:
        sign.append('-')
    elif check > num:
        temp = False
        break
    else:
        stack.append(check)
    
if temp:
    print(*sign, sep='\n')
else:
    print('NO')