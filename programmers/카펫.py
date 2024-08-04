# 12~39
# 갈색 격자의 수 brown, 노란색 격자의 수 yellow
# 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return

# 카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.
# 가로 >= 세로 길이

# 10 2 [4,3]
#  x*y = brown + yellow
# 2x + (2y-4) = brown
## xy = 12
## 2x + 2y -4 = 10
## x + y -2 = 5
## x + y = 7

# 8, 1 [3,3]
# xy = 9
# x +y =6



# x*y = brown + yellow
# 2x + (2y-4) = brown
def solution(brown, yellow):
    answer = []
    sum = brown + yellow
    a = 0
    b = 0
    for x in range(1, sum + 1):
        if sum % x == 0:  # x가 sum의 약수인지 확인
            y = sum // x  # y 계산
            if 2*x + (2*y-4) == brown:
                    a = x
                    b = y
                    break
                    
    if a >= b:
        answer.append(a)
        answer.append(b)
    else:
        answer.append(b)
        answer.append(a)
    return answer