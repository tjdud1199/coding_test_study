import sys

input = sys.stdin.readline

n = int(input().rstrip())

if n > 198:
    print(0)
else:
    result = 0
    for i in range(1, 100):
        if n-i < 100:
            result += 1
    print(result)