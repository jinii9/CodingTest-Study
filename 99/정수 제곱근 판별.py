import math

n = int(input())

value = int(math.sqrt(n))

if math.pow(value, 2) == n:
    print(int(math.pow(value + 1, 2)))
else:
    print(-1)