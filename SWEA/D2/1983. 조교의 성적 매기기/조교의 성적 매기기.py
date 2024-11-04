t = int(input())

for i in range(1, t+1):
    n, k = map(int, input().split())
    total_scores = []
    scores = ['A+','A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    
    for j in range(1,n+1):
        mid, final, work = map(int, input().split())
        total_scores.append((j,mid*0.35+final*0.45+work*0.2))
    total_scores.sort(key=lambda x: x[1], reverse=True)
    
    for idx, (stu_num, _) in enumerate(total_scores):
        if stu_num == k:
            score_idx = idx//(n//10)
            print('#'+str(i),scores[score_idx])
            break