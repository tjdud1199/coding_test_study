import sys

input = sys.stdin.readline

obj = input().rstrip()
n = int(input().rstrip())
result = 0

for _ in range(n):
    check = input().rstrip()
    if obj in check*2:
        result += 1

print(result)