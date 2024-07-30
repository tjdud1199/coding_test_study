import sys
input = sys.stdin.readline

K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]

start = 0
end = max(arr)

while(start <= end):
    total = 0
    mid = (start + end+1) // 2
    
    for lan in arr:
        total += lan // mid

    if total < N:
        end = mid - 1

    else:
        start = mid + 1

print(end)