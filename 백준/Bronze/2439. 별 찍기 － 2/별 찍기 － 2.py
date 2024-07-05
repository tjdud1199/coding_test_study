
import sys

input = sys.stdin.readline

n = int(input().rstrip())

for i in range(1, n+1):
    star = '*'*i
    print(star.rjust(n))