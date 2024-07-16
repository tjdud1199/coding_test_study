import sys

input = sys.stdin.readline

a, b, v = map(int, input().split())
cnt = (v - a) // (a-b) + 1

if (v-a) % (a-b) != 0:
    cnt += 1

print(cnt)