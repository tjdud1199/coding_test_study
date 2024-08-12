import sys
from collections import deque

input = sys.stdin.readline
n = int(input().rstrip())
graph = [[] for _ in range(n+1)]

for _ in range(int(input().rstrip())):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
visited = [False for _ in range(n+1)]

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

bfs(graph, 1, visited)
print(visited.count(True)-1)