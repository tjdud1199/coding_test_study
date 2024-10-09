n = int(input())
result = []

for i in range(1, int(n**(1/2))+1):
    if n%i == 0:
        result.append(i)
        if i < n//i:
            result.append(n//i)

result.sort()
print(*result, sep=' ')