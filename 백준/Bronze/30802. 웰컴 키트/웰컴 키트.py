import sys

input = sys.stdin.readline

n = int(input().rstrip())
sizes = list(map(int, input().split()))
t, p = map(int, input().split())
result = 0

for size in sizes:
    if size % t == 0:
        result += size//t
    else:
        result += size//t + 1

print(result)
print(n//p, n%p)