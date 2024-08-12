# - * 3^N
# 가운대 문자열 3^N//3
# f(0) = -
## 0
# f(1) = f(0) + '' + f(0)
## 1
# f(2) = f(1) + '' + f(1)
## 3
# f(3) = f(2) + '' + f(2)
## 9



def sol(x):
    if x == 0:
        return '-'
    return sol(x-1) + ' '*(3**x//3) + sol(x-1)

while True:
    try:
        N = int(input())
        print(sol(N))
    except:
        break
