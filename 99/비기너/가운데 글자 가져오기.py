def solution(s):
    answer = ''
    length = len(s)

    if length % 2 != 0:  # 홀수
        answer = s[length // 2]
    else:  # 짝수
        answer = s[length // 2 - 1] + s[length // 2]
        print("s")

    return answer