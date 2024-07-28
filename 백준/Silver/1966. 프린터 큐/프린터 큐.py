import sys
from collections import deque

t = int(input().rstrip())
for _ in range(t):
    n, m = map(int, input().split())
    docs = list(map(int, input().split()))
    queue = deque([(i,p) for i, p in enumerate(docs)])
    cnt = 0
    
    while True:
        i, p = queue.popleft()
        if p == max(docs):
            cnt += 1
            docs.remove(p)
            if i == m:
                print(cnt)
                break
        else:
            queue.append((i,p))