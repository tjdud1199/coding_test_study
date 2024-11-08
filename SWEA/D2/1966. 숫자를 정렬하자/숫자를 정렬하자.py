t = int(input())

for i in range(1, t+1):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    print(f"#{i}", *nums)