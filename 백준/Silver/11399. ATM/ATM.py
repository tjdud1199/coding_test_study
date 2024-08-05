import sys

input = sys.stdin.readline

n = int(input().rstrip())
P = sorted(list(map(int, input().split())))

i = 0
result = 0
for p in P:
    i += p
    result += i
print(result)