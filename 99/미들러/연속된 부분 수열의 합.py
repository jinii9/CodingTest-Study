# 40 ~
# 정수 배열 sequence
# 부분 수열의 합 k
# 위 조건 만족하는 부분 수열의 시작 인덱스, 마지막 인덱스 배열
# 합이 여러 개인 경우, 길이 짧은 거
# 길이가 짧은 게 여러 개인 경우, 시작 인덱스가 작은 거
# 1 2 3 4 5
# 7

# 로직
# 합이 k인 수열 찾기

def solution(sequence, k):
    answer = []
    sum_idx = []
    minIdx = []
    value = 0

    for i in range(len(sequence)):  # 1 2 3 4 5
        for j in range(i, len(sequence)):
            value += sequence[j]
            sum_idx.append(j)  # 인덱스
            if value == k:
                if len(minIdx) == 0:
                    minIdx = sum_idx
                # 여러 개인 경우 길이가 짧은 수열 찾기 & 길이가 짧은 수열이 여러 개인 경우 시작 인덱스 비교
                elif len(sum_idx) < len(minIdx):
                    minIdx = sum_idx
                elif len(minIdx) == len(sum_idx):
                    if minIdx[0] > sum_idx[0]:
                        minIdx = sum_idx

                sum_idx = []
                value = 0

        sum_idx = []
        value = 0

    answer.append(minIdx[0])
    answer.append(minIdx[len(minIdx) - 1])

    return answer