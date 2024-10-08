import sys

input = sys.stdin.readline
fizzbuzz = []
for _ in range(3):
    fizzbuzz.append(input().rstrip())

for i in range(3):
    word = fizzbuzz[i]
    if word.isdigit():
        result = int(word) + 3 - i
        if result % 3 == 0 and result % 5 == 0:
            print("FizzBuzz")
        elif result % 3 == 0:
            print("Fizz")
        elif result % 5 == 0:
            print("Buzz")
        else:
            print(result)
        break