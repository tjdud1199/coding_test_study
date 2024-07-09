import sys

input = sys.stdin.readline

n = int(input().rstrip())
words = []

for _ in range(n):
    words.append(input().rstrip())

words = sorted(list(set(words)), key=lambda x: (len(x), x))

for i in words:
    print(i)