n = int(input())
res = []
num_369 = ['3', '6', '9']

for i in range(1, n+1):
    i = str(i)
    if ('3' in i) or ('6' in i) or ('9' in i):
        cnt_dict = {num: i.count(num) for num in num_369}
        cnt_369 = sum(cnt_dict.values())
        i = str('-'*cnt_369)
    res.append(i)

print(*res)