# N개의 물건
# 무게 W, 가치 V -> V만큼의 즐거움
# 최대 K만큼의 무게 배낭
# 배낭에 넣을 수 있는 물건들의 가치의 최댓값

# N 물품 수 / K 버틸 수 있는 무게
# N개의 줄 - W무게 V가치

# 브루트포스 : 2^100,000
# DP
# dp[n] = N개까지의 가치

# 4 7

# 6 13
# 4 8
# 3 6
# 5 12

# dp[1] 물품 1개 : max(1)
# dp[2] : dp[]

# dp[w] = w 무게까지의 최대 가치
# dp[w] = max(w가 n인 무게, )
# dp[1] = 20
# dp[2] = 0
# dp[3] = 6
# d[4] = max(8, 20+6)
# d[5] = max(12, 8+20)
# d[6] = 


# 1 2 3 4 5
# dp[n][w] = 물품 n개, 무게 w 이하일 때의 최대 가치값
# dp[3][10] = max(dp[2][10], dp[3][10-3의 무게]+8)
# 이전의 최대 가치에 지금 물건의 가치를 더하기




N, K = map(int, input().split())
W = [0]
V = [0]
for _ in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)
    
dp = [[0] * (K + 1) for _ in range(N + 1)]


for n in range(1, N + 1):
    for k in range(K + 1):
        dp[n][k] = dp[n-1][k]
        if k - W[n] >= 0:
            dp[n][k] = max(dp[n][k], dp[n-1][k-W[n]] + V[n])

print(dp[N][K])

