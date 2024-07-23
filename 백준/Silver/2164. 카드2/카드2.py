import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())
cards = [i for i in range(1, n+1)]
cards = deque(cards)

while len(cards) > 1:
    cards.popleft()
    cards.rotate(-1)

print(cards.popleft())