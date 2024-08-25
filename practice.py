# 평범한 배낭
# N개의 물건
# 무게W 가치V
# 최대 K만큼의 무게
# 가치의 최댓값 구하기

# 물품 개수 N, 버틸 수 있는 무게 K
# 무게 W, 가치 V

# dp[N][W] = 물품 N개의 W무게 이하의 최대 가치값
# dp[n][w] = max(dp[n-1][w], dp[n][w])
# 물품 n-1개의 w무게 이하의 최대 가치값
# 물품 n 개의 해당 w무게 더한 최대 가치값

N, K = map(int, input().split())
arr = [[0, 0]]
arr += [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (K+1) for _ in range(N + 1)]

for n in range(1, N+1): # 물품 수
    for w in range(1, K+1): # 무게
        now_w, now_v = arr[n]

        dp[n][w] = dp[n-1][w]
        if w - now_w >= 0:
            # dp[n][w] = max(dp[n-1][w], dp[n-1][w] + now_v)
            dp[n][w] = max(dp[n][w], dp[n-1][w-now_w] + now_v)

print(dp[N][K])