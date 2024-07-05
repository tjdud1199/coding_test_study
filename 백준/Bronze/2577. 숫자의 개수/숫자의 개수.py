import sys

input = sys.stdin.readline
result = 1

for _ in range(3):
    result *= int(input().rstrip())
result = str(result)

for i in range(10):
    print(result.count(str(i)))