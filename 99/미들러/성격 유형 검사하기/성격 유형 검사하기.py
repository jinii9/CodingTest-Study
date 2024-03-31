# 단, 하나의 지표에서 각 성격 유형 점수가 같으면, 두 성격 유형 중 사전 순으로 빠른 성격 유형을 검사자의 성격 유형이라고 판단
# 1번 지표	라이언형(R), 튜브형(T)
# 2번 지표	콘형(C), 프로도형(F)
# 3번 지표	제이지형(J), 무지형(M)
# 4번 지표	어피치형(A), 네오형(N)

# 질문마다 판단하는 지표를 담은 1차원 문자열 배열 survey
# 검사자가 각 질문마다 선택한 선택지를 담은 1차원 정수 배열 choices

# ["AN", "CF", "MJ", "RT", "NA"]	[5, 3, 2, 7, 5]	"TCMA"
def output(type):
    print(type)
    s = ''
    # 0 2 4 6

    for i in range(0, 7, 2):
        if type[i][1] > type[i + 1][1]:  # 앞에가 더 큰 경우에
            s += type[i][0]
        elif type[i][1] < type[i + 1][1]:
            s += type[i + 1][0]
        elif type[i][1] == type[i + 1][1]:  # 같은 경우에
            if type[i][0] < type[i + 1][0]:
                s += type[i][0]
            else:
                s += type[i + 1][0]

    #     type.sort(key=lambda x: (-x[1], x[0]))  # score가 높은 순
    #     # type[:4].sort(key=lambda x: x[0])
    print(s)
    return s


def solution(survey, choices):
    type = [['R', 0], ['T', 0], ['C', 0], ['F', 0], ['J', 0], ['M', 0], ['A', 0], ['N', 0]]
    scores = [3, 2, 1, 0, 1, 2, 3]
    answer = ''

    for i in range(len(survey)):  # AN
        choice = choices[i]
        if choice < 4:
            for j in range(len(type)):  # 해당 성격 점수 올려주기
                if type[j][0] == survey[i][0]:
                    type[j][1] += scores[choice - 1]
                    # print(type)
        elif choice > 4:
            for j in range(len(type)):  # 해당 성격 점수 올려주기
                if type[j][0] == survey[i][1]:
                    type[j][1] += scores[choice - 1]
                    # print(type)

    # type.sort(key=lambda x: (-x[1], x[1]), reverse=True)
    answer = output(type)
    return str(answer)

# 튜플은 값 변경이 불과하다!
# 귀찮아도 문제 제발 끝까지, 똑바로 읽자. 특히 예시 나온거 잘 읽고...! plz.. -> 비동의 관련 선택지를 선택하면 어피치형(A) 성격 유형의 점수를 얻고, 동의 관련 선택지를 선택하면 네오형(N) 성격 유형의 점수