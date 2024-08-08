import sys

input = sys.stdin.readline

n, m = map(int, input().split())
memo = {}

for _ in range(n):
    address, passwd = input().split()
    memo[address] = passwd

for _ in range(m):
    site = input().rstrip()
    print(memo[site])