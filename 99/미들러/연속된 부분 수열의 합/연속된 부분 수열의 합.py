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

# 시간 초과 판정 이유
# 1. 중첩 반복문 : sequence의 길이가 n일 때, 대략 O(n^2)의 시간 복잡도 -> n이 큰 경우, 매우 느리게 작동
# 2. 불필요한 배열 생성&복사 : 각 반복마다 sum_idx 배열을 생성하고, 조건에 맞는 경우 minIdx에 복사
# 3. 불필요한 초기화 : 각 외부 반복마다 내부 반복문이 끝난 후 sum_idx와 value를 초기화

## 즉, 시작 인덱스, 마지막 인덱스만 필요하므로, 배열로 구할 필요가 없다!
## 길이 비교는 '마지막idx-시작idx'로 구하면 된다!

# => 투 포인터 알고리즘 사용: 투 포인터 알고리즘을 사용하면 중첩 반복문 없이 배열을 한 번만 순회하면서 문제를 해결 -> O(n)의 시간 복잡도
