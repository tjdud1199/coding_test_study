import sys

input = sys.stdin.readline

n = int(input().rstrip())
result = []

for _ in range(n):
    result.append(int(input().rstrip()))
    
result.sort()
print(*result, sep='\n')