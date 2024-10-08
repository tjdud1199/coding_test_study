import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())

deq = deque()

for _ in range(n):
    order = input().split()
    if order[0] == 'push_front':
        deq.appendleft(int(order[1]))
    elif order[0] == 'push_back':
        deq.append(int(order[1]))
    elif order[0] == 'pop_front':
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif order[0] == 'pop_back':
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(deq))
    elif order[0] == 'empty':
        if deq:
            print(0)
        else:
            print(1)
    elif order[0] == 'front':
        if deq:
            print(deq[0])
        else:
            print(-1)
    else:
        if deq:
            print(deq[-1])
        else:
            print(-1)