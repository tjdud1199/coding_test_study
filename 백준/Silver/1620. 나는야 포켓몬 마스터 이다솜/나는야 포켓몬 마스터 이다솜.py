import sys

input = sys.stdin.readline

n, m = map(int, input().split())
idx_dic = {}
name_dic = {}
for i in range(1, n+1):
    name = input().rstrip()
    idx_dic[i] = name
    name_dic[name] = i

for _ in range(m):
    check = input().rstrip()
    if check.isdigit():
        print(idx_dic[int(check)])
    else:
        print(name_dic[check])