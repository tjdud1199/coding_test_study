import sys

input = sys.stdin.readline

n = int(input().rstrip())
cnt = 1
i_max = 1

while True:
    if i_max < n:
        i_max += 6*cnt
        cnt += 1
    if i_max >= n:
        print(cnt)
        break