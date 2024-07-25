import sys

input = sys.stdin.readline

n = int(input().rstrip())
stack = []

for _ in range(n):
    order = list(input().split())
    if len(order) == 2:
        type, num = order[0], int(order[1])
    else:
        type = order[0]
    
    if type == 'push':
        stack.append(num)
    elif type == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif type == 'size':
        print(len(stack))
    elif type == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)