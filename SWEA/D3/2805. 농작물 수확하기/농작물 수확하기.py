t = int(input())

for i in range(1, t+1):
    n = int(input())
    res = 0
    if n == 1:
        res = int(input())
        print(f"#{i} {res}")
        continue
    harvests = [[int(x) for x in input()] for _ in range(n)]
    res += sum(harvests[n//2])
    idx = 0
    for j in range(n//2,0,-1):
        res += sum(harvests[idx][j:n-j])
        res += sum(harvests[n-1-idx][j:n-j])
        idx += 1
    print(f"#{i} {res}")