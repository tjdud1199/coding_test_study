import sys

input = sys.stdin.readline

T = int(input().rstrip())

# h = 층, w = 방 개수, n = 순서
# 6, 12, 10
# 30 50 72 
for _ in range(T):
    h, w, n = map(int, input().split())
    room = n // h + 1
    floor = n % h
    if floor == 0:
        floor = h
        room -= 1
    print(floor*100 + room)