import sys
import math

input = sys.stdin.readline

n = int(input().rstrip())
nums = list(map(int, input().split()))
result = 0

def isPrime(n):
    if n == 1:
        return False
    # 2부터 제곱근까지 모든 수 확인
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
    
for num in nums:
    if isPrime(num):
        result += 1

print(result)