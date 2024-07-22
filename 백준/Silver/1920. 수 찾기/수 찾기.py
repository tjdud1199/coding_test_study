import sys

input = sys.stdin.readline

n = int(input().rstrip())
A = list(map(int, input().split()))
m = int(input().rstrip())
X = list(map(int, input().split()))

result = {}

for a in A:
    result[a] = 1

for x in X:
    print(result.get(x, 0))