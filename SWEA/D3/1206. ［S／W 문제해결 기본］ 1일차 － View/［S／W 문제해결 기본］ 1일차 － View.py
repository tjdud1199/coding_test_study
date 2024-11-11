for i in range(1, 11):
    n = int(input())
    heights = list(map(int, input().split()))
    cnt = 0
    
    for j in range(2, n-2):
        now_b = heights[j]
        max_b = max(*heights[j-2:j], *heights[j+1:j+3])
        if now_b > max_b:
            cnt += now_b-max_b
    
    print(f"#{i} {cnt}")