import sys
import string

input = sys.stdin.readline

alpha = string.ascii_lowercase

L = int(input().rstrip())
text = input().rstrip()
r = 31
M = 1234567891

result = 0

for i in range(L):
    word = text[i]
    a = alpha.find(word) + 1
    result += a*r**i

print(result%M)