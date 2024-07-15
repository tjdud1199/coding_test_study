import sys
import string

input = sys.stdin.readline

n = int(input().rstrip())
members = []

for i in range(n):
    members.append([i, *input().split()])

members.sort(key=lambda x: (int(x[1]), x[0]))

for member in members:
    print(member[1], member[2])