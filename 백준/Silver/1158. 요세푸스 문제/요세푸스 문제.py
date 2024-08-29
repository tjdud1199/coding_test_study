import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
circle = deque([i for i in range(1, n+1)])
result = []

for _ in range(n):
    circle.rotate(-(k-1))
    result.append(str(circle.popleft()))

print('<'+', '.join(result)+'>')