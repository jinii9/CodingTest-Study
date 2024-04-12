# 20~
# 문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현하여 더 짧은 문자열로 줄여서 표현하는 알고리즘
# aabbaccc -> 2a2ba3c

# ababcdcdababcdcd

# 2개의 단위로 잘라서 -> 2ab2cd2ab2cd
# 8개 단위로 잘라서 -> 2ababcdcd

# abcabcdede
# 2개 -> abcabc2de
# 3개 -> 2abcdede

# 로직
# 문자열 개수 범위 : s 길이
# 1 -> 알파벳 종류 개수 + 연속되는 것끼리 개수 구하기 + 1개일 경우의 개수
# 2 -> ab
# 문자열 종류 구하기 a b c d
# 문자열 조합 구하기 ab ac ad / abc ...
#

#
def solution(s): # abcabcdede
    if len(s) == 1: # 빼먹으면 '런타임 에러'남!
        return 1

    temp = s # 복사
    length = 0
    kinds = [] # 알파벳 종류
    answers = []

    while length < len(s)-1:
        length += 1 # 2
        # count = len(s) // length # 5
        # print("length", length)

        # kinds에 1,2,3개별로 자르기
        for i in range(0, len(s), length): #2개씩 0 2 4
            kinds.append(s[i:i + length])

        print(kinds)

        count = list(set(kinds))
        # 각 요소를 문자열 키와 값이 0인 딕셔너리로 변환
        # count_dict = [{str(item): 0} for item in count]

        # print(count_dict)

        # kinds끼리 똑같은게 있는지
        target = 0
        target_cnt = 1
        result_s = ""

        for i in range(len(kinds)):
            target = kinds[i]

            # if (i + 1) == len(kinds)-1:

            # if len(kinds)-1 == 1: # 배열이 단 2개일 경우
            #     target_cnt += 1
            #     result_s += str(target_cnt) + str(target)

            # if kinds[i] == kinds[i + 1]:
            #     target_cnt += 1
            #     print("target_cnt", target_cnt)
            if i + 1 < len(kinds) and kinds[i] == kinds[i + 1]:
                target_cnt += 1

            else: # 다를 때
                if target_cnt > 1: # 1보다 클 때
                    result_s += str(target_cnt) + str(target)
                else: # 1일 때
                    result_s += str(target)
                target_cnt = 1 # 롤백

        print(result_s)
        answers.append(len(result_s))
        kinds = []
    return min(answers)

# s = input()
# 테스트 케이스
s = 'aabbaccc'
print(solution(s))  # 7

s = 'abcabcdede'
print(solution(s))  # 8

s = 'ababcdcdababcdcd'
print(solution(s))  # 9

#########################################
# 처음에 set, 딕셔너리 쓰면서까지 굳이굳이 코드를 나눠서 하나씩 계산 했다..

# if (i + 1) == len(kinds)-1: -> 이렇게 하나하나 조건문으로 따로 빼지 말고
# if i + 1 < len(kinds) and kinds[i] == kinds[i + 1]: -> 이런 식으로 반대 조건일 경우로 해주기!

# 나는 step을 s의 길이만큼 해줬는데, 문자열이 절반 이상으로 잘렸을 때는 어떤 경우에도 1번 이상 반복될 수 없으므로 len//2만큼 단위만 구해줘도 된다!




