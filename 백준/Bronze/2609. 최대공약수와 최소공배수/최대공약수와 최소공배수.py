import sys

input = sys.stdin.readline

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
    
def lcd(a, b):
    return abs(a*b) // gcd(a, b)

a, b = map(int, input().split())

print(gcd(a, b))
print(lcd(a, b))