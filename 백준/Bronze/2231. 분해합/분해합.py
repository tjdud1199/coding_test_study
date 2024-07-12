import sys

input = sys.stdin.readline

n = int(input().rstrip())
found = False

for i in range(1, n):
    n_sum = i
    n_sum += sum(list(map(int, str(i))))
    if n_sum == n:
        print(i)
        found = True
        break

if not found:
    print(0)