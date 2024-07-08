import sys
import string

input = sys.stdin.readline

S = input().rstrip()
alpha = list(string.ascii_lowercase)
result = []

for word in alpha:
    result.append(S.find(word))

print(*result)