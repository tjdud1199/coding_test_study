import sys

input = sys.stdin.readline

n = int(input().rstrip())
n_card = list(map(int, input().split()))
m = int(input().rstrip())
m_card = list(map(int, input().split()))

dic = {}

for i in n_card:
    dic[i] = dic.get(i, 0) + 1

result = []
for i in m_card:
    result.append(dic.get(i, 0))

print(*result)