import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())
queue = deque()

for _ in range(n):
    order = list(input().split())
    if len(order) == 2:
        queue.append(order[1])
    else:
        type = order[0]
        if type == 'pop':
            if queue:
                print(queue.popleft())
            else:
                print(-1)
        elif type == 'size':
            print(len(queue))
        elif type == 'empty':
            if queue:
                print(0)
            else:
                print(1)
        elif type == 'front':
            if queue:
                print(queue[0])
            else:
                print(-1)
        else:
            if queue:
                print(queue[-1])
            else:
                print(-1)