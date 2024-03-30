# 2555
# 325

# 1,2,3,4 => -1
# 6,7,8,9 => +1
# 5 => 다음 자릿수 확인

def solution(storey):
    answer = 0
    while storey != 0:
        one = storey % 10  # 1의 자리
        ten = (storey // 10) % 10  # 10의 자리 (# 다음 자릿수 확인 위해 현재 자릿수 제거)
        if one < 5:
            answer += one
            storey -= one
        elif one > 5:
            answer += (10 - one)
            storey += (10 - one)
        else:  # 5일 경우 -> 현재 자릿수가 5일 때 다음 자릿수(십의 자리)에 따라 최적의 행동이 달라지기 때문
            if ten < 5: # 일의 자리, 즉 현재 n의 다음 자릿수가 5 이하인지를 확인
                answer += one
                storey -= one
            else:
                answer += (10 - one)
                storey += (10 - one)

        storey //= 10  # (중요!!!) 자릿 수 높이기 (1의 자리 -> 10의 자리 ...)

    print(answer)
    return answer

###############################################
# 정말 어려워요.

