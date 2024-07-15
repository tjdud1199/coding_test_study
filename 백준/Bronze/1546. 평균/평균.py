import sys

input = sys.stdin.readline

n = int(input().rstrip())
scores = list(map(int, input().split()))
result = 0
M = max(scores)

for score in scores:
    result += score/M*100

print(result/n)