import sys

input = sys.stdin.readline

t = int(input().rstrip())
result = []

for _ in range(t):
    a, b = map(int, input().split())
    result.append(a+b)

for num in result:
    print(num)