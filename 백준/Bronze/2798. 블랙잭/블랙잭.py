import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))

sums = [sum(nC3) for nC3 in list(combinations(cards, 3))]
sums.sort()
m_max = 0
for i in sums:
    if i > m_max and i <= m:
        m_max = i
    if i > m:
        break
print(m_max)