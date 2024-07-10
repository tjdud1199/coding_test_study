import sys

input = sys.stdin.readline

n = int(input().rstrip())
i = 666
check = 1

while True:
    if check == n:
        break
    i += 1
    if '666' in str(i):
        check += 1

print(i)