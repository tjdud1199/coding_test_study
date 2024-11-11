for i in range(1, 11):
    d = int(input())
    boxes = list(map(int, input().split()))
    boxes.sort()

    for _ in range(d):
        boxes[0] += 1
        boxes[-1] -= 1
        boxes.sort()
    
    print(f"#{i} {boxes[-1]-boxes[0]}")