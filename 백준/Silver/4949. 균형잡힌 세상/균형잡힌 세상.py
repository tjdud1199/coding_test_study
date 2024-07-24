import sys

input = sys.stdin.readline

while True:
    text = input().rstrip()
    if text == '.':
        break
    
    check = []
    result = 'yes'
    for t in text:
        if t == '(' or t == '[':
            check.append(t)
        elif t == ')':
            if check:
                if check.pop() != '(':
                    result = 'no'
                    break
            else:
                result = 'no'
                break
        elif t == ']':
            if check:
                if check.pop() != '[':
                    result = 'no'
                    break
            else:
                result = 'no'
                break
        if t == '.':
            if check:
                result = 'no'
                break
    print(result)
