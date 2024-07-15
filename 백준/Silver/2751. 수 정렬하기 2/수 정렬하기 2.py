import sys

input = sys.stdin.readline

n = int(input().rstrip())
result = [int(input().rstrip()) for _ in range(n)]
    
result.sort()
print(*result, sep='\n')