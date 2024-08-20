# 27~
# 집 N 개
# 1~N번 집
# 모든 집 칠하는 비용 최솟값

# 빨강 초록 파랑
# 1번 집 != 2번 집 색
# N번 집 != N-1번 집 색
# i-1 집 식 != i번 집 != i+1 집 색

# 집 3개
# 빨강 초록 파랑

# 브루스포스 : 3^1000
# 그리디 : X
# DP : 

# 1번집이 빨강, 초록, 파랑
# f(x) = min(f(x-1))
# dp[][]
# dp[0][] 빨강
# dp[1][] 초록
# dp[2][] 파랑

# 빨,초 파랑 초록 -> 빨, 파
# f(초) = min(f(파), f(빨))
# 26 57 13

#  dp 빨 = min(dp 파 , dp 초)
# 
N = int(input())
homes = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(3)] for _ in range(N)]

for i in range(3):
    dp[0][i] = homes[0][i]
# print(dp)

# 빨
# dp[i][j] = dp[i-1][j+1], dp[i-1][j+2]
# 초
# dp[i][j] = dp[i-1][j-1], dp[i-1][j+1]
# 파
# dp[i][j] = dp[i-1][j-2], dp[i-1][j-1]
for i in range(1, N):
    for j in range(3):
        if j == 0: # 빨
            dp[i][j] += min(dp[i-1][j+1], dp[i-1][j+2]) + homes[i][j]
        elif j == 1: # 초
            dp[i][j] += min(dp[i-1][j-1], dp[i-1][j+1]) + homes[i][j]
        elif j == 2: # 파
            dp[i][j] += min(dp[i-1][j-2], dp[i-1][j-1]) + homes[i][j]
        # print(dp[i][j])


print(min(dp[N-1][0], dp[N-1][1], dp[N-1][2]))

