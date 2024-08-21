# LCS
# ACAYKP
# CAPCAK
# d[n][m]
# ABDEA
# DAWEF
# 같을 경우 : d[n-1][m-1] + 1
# 다를 경우 : d[n-1][m], d[n][m-1]

S1 = input()
S2 = input()

N, M = len(S1), len(S2)
s1 = " " + S1
s2 = " " + S2

dp = [[0] * (M+1) for _ in range(N+1)]

# 초기값
#

for i in range(1, N+1):
    for j in range(1, M+1):
        if S1[i] == S2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[N][M])