import sys
import heapq

input = sys.stdin.readline

n = int(input().rstrip())
heap = []

for _ in range(n):
    heapq.heappush(heap, int(input().rstrip()))

for _ in range(n):
    print(heapq.heappop(heap))