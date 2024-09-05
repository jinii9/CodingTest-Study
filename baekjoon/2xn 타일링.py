# 2xn
# 2x1
# 1x2
# dp[n] = dp[n-1] + dp[n-2]

N = int(input())
dp = [0] * (N + 2) # 크기를 (N+1)로 지정하면, N이 1이면, dp[2]는 없기 때문에

dp[1] = 1
dp[2] = 2

for i in range(3, N+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007

print(dp[N])