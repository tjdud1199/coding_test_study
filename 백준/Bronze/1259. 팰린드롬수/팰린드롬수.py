import sys

input = sys.stdin.readline

while True:
    num = input().rstrip()
    if int(num) == 0:
        break
    if list(reversed(num)) == list(num):
        print('yes')
    else:
        print('no')