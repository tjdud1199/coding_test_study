import sys

input = sys.stdin.readline

n = int(input().rstrip())
n_fac = 1
for i in range(1, n+1):
    n_fac *= i

num_0 = 0
for i in str(n_fac)[::-1]:
    if i == '0':
        num_0 += 1
    else:
        print(num_0)
        break