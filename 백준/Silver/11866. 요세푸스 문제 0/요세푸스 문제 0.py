import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
a = [i+1 for i in range(n)]
deq = deque(a)
result = []

while deq:
    deq.rotate(-(k-1))
    result.append(str(deq.popleft()))

print('<'+', '.join(result)+'>')