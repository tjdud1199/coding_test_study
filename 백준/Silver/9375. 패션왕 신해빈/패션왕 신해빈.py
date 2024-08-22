import sys
from itertools import combinations
import math

input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    clothes = {}
    n = int(input().rstrip())
    for _ in range(n):
        cloth, type = input().split()
        clothes[type] = clothes.get(type, 0) + 1
    result = 1
    for count in clothes.values():
        result *= count+1
    print(result-1)