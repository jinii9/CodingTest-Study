def solution(dp, row, col):
    # 오른쪽 위
    # 오른쪽
    # 오른쪽 아래
    # for a in range(0, row):
    #     for b in range(1, col): # 2번째 열부터
    for b in range(1, col):
        for a in range(row): # 2번째 열부터
            # 왼쪽
            left = dp[a][b-1]

            # 왼쪽 위
            if a - 1 < 0:
            # if a == 0: ## -> 이렇게도 조건 가능
                left_up = 0
            else:
                left_up = dp[a-1][b-1]

            # 왼쪽 아래
            if a + 1 >= row:
            # if a == row - 1: ## -> 이렇게도 조건 가능
                left_down = 0
            else:
                left_down = dp[a+1][b-1]


            dp[a][b] += max(left, left_up, left_down)
    return dp

for T in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    dp = []
    i = 0
    for _ in range(n):
     dp.append(arr[i:i + m]) # i:i+m은 i번째 위치부터 i+m번째 위치 전까지
     i += m

    dp = solution(dp, n, m)
    print(dp)

    print(max(dp[a][m-1] for a in range(n)))
################################
# [review]
# 점화식은 맞았다만 자잘한 실수가 너무 많았다.

# [개선]
## 1. 입력 부분
### before
# T = int(input())
# dp = []
# for _ in range(T):
#     n, m = map(int, input().split())
#     dp = [[0] * (m + 1) for _ in range(n + 1)]
#
#     arr = list(map(int, input().split()))
#     i = 0
#     for a in range(1, n + 1):
#         for b in range(1, m + 1):
#             dp[a][b] = arr[i]
#             i += 1

## 2. 로직 부분
### 이 방식은 현재 위치에서 가능한 최대 금의 양을 정확히 계산하지 못함. -> 정확한 계산을 위해서는 현재 위치에 도달하기 전, 즉 이전 열에서 오른쪽 위, 바로 왼쪽, 오른쪽 아래 중 최대 값을 선택하여 현재 값에 더해야 한다.
### before
# for a in range(0, row):
#     for b in range(1, col): # 2번째 열부터
#         # 오른쪽
#         dp[a][b] = dp[a][b-1] + dp[a][b]
#         # 오른쪽 위
#         if a - 1 >= 0:
#             dp[a][b] = max(dp[a][b], dp[a-1][b-1] + dp[a][b])
#         # 오른쪽 아래
#         if a + 1 < row:
#             dp[a][b] = max(dp[a][b], dp[a+1][b-1] + dp[a][b])

###(!!!중요) '행' 우선 순회가 아닌 이유 : 만약 행 우선 순회를 했다면, 특정 행의 모든 열을 계산한 후 다음 행으로 넘어가게 된다. 이 경우, 현재 위치에서 필요한 "왼쪽 위"나 "왼쪽 아래"의 정보가 아직 계산되지 않은 상태일 수 있기 때문
### before
# def solution(dp, row, col):
#     # 오른쪽 위
#     # 오른쪽
#     # 오른쪽 아래
#     for a in range(0, row):
#         for b in range(1, col):  # 2번째 열부터
#             # 왼쪽
#             left = dp[a][b - 1]
#             # 왼쪽 위
#             if a - 1 >= 0:
#                 left_up = dp[a - 1][b - 1]
#             # 오른쪽 아래
#             if a + 1 < row:
#                 left_down = dp[a + 1][b - 1]
#
#             dp[a][b] += max(left, left_up, left_down)
#     return dp
