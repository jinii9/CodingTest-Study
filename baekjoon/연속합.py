# 연속된 몇 개의 수 
# 가장 큰 합

# 1. 브루트포스
# nC2 * n

# 2. DP
# 10 -4 3 1 5 6 -35 12 21 -1 14
# 10 -1 4 
# dp[n] = n에서 끝나는 or n까지 살펴봤을 때
# dp[10] = 33
# dp[11] = 
# dp[n] = max(0, dp[n-1]) + arr[n]

n = int(input())
arr = [0] + list(map(int, input().split()))

dp = [0] * (n+1)

for i in range(1, n + 1):
    dp[i] = max(0, dp[i-1]) + arr[i]

print(max(dp[1:]))
