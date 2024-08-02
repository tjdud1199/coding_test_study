import sys

input = sys.stdin.readline

n, m = map(int, input().split())

un_heard = set([input().rstrip() for _ in range(n)])
un_seen = set([input().rstrip() for _ in range(m)])

result = un_heard & un_seen
print(len(result))
print(*sorted(list(result)), sep='\n')