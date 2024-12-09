# dp
# dp[n] = dp[n-2] * 3

dp = [0] * 31 # dp=[0]*30으로 할 경우, dp[30]은 존재 X -> 런타임 에러

N = int(input())

dp[0] = 1

for n in range(2, 31, 2):
    dp[n] = dp[n-2] * 3
    for i in range(n-4, -1, -2):
        dp[n] += dp[i] * 2


print(dp[N])