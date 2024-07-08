import sys

input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    R, S = input().split()
    result = ''
    for word in S:
        result += word*int(R)
    print(result)