t = int(input())
tri = [[1], [1, 1], [1, 2, 1]]

for i in range(1, t+1):
    tri = [[1], [1, 1], [1, 2, 1]]
    n = int(input())
    if n > 3:
        for j in range(3, n):
            pre = tri[j-1]
            new = [1] + [pre[x-1]+pre[x] for x in range(1, j)] + [1]
            tri.append(new)
    print(f"#{i}")
    for nums in tri[:n]:
        print(*nums)
            