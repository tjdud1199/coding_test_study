import sys

input = sys.stdin.readline

S = set()

m = int(input().rstrip())
for _ in range(m):
    op = input().split()
    if len(op) == 2:
        type, num = op[0], int(op[1])
        if type == 'add':
            S.add(num)
        elif type == 'remove':
            S.discard(num)
        elif type == 'check':
            if num in S:
                print(1)
            else:
                print(0)
        else:
            if num in S:
                S.remove(num)
            else:
                S.add(num)
    else:
        if op[0] == 'all':
            S = set([i for i in range(1, 21)])
        else:
            S = set()