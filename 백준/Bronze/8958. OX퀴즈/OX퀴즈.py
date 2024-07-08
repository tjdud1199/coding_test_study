import sys

input = sys.stdin.readline

t = int(input().rstrip())

for _ in range(t):
    result = input().rstrip()
    now = result[0]
    score = 0
    i = 0
    for ox in result:
        if ox == 'X':
            i = 0
            now = ox
        else:
            if now == ox:
                i += 1
            else:
                i = 1
                now = ox
        score += i
    print(score)