import sys
import math

input = sys.stdin.readline

n = int(input().rstrip())

if n == 0:
    result = 0
else:
    scores = [int(input().rstrip()) for _ in range(n)]
    scores.sort()
    idx = math.floor(n*0.15+0.5)
    result = math.floor(sum(scores[idx:len(scores)-idx])/(len(scores)-idx*2)+0.5)
print(result)