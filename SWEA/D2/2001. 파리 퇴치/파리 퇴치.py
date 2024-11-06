t = int(input())

def prefix_sum(n, arr):
    prefix = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            prefix[i][j] = prefix[i][j-1] + prefix[i-1][j] + arr[i-1][j-1] - prefix[i-1][j-1]
    return prefix

for i in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    prefix = prefix_sum(n, arr)
    
    m_sum = []
    for x in range(m,n+1):
        for y in range(m, n+1):
            flies = prefix[x][y] - prefix[x-m][y] - prefix[x][y-m] + prefix[x-m][y-m]
            m_sum.append(flies)
    print('#'+str(i), max(m_sum))