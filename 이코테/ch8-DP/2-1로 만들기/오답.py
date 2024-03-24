# 19분~
x = int(input())
d = [0] * 30000
d[x] = x

while x != 1:
    if x % 5 == 0:
        d[x//5] = x // 5
    elif x % 3 == 0:
        d[x//3] = x // 3
    elif x % 2 == 0:
        d[x//2] = x // 2
    else:
        d[x] = x - 1
    