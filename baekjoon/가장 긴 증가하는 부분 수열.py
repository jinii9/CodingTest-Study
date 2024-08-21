# 50~
# 10 20 10 30 20 50

# 10 20 30 50

# 10 20 20 10 30 50
# 10 20 30 50
# 20 30 50
# 20 30 50

# 브루스투스 : 2^1000
# 그리디 : 1000!

# DP : 부분수열 f(x번째 자리) = max(f(x-1번째 자리), )
# f(x)는 부분수열 x의 최대 개수

# dp[n] : n번째까지 살펴봤을 떄의 LIS

# dp[n-1] : n-1번째까지

# dp[n-2]

# dp[0] = 10 20 10 30 20 50
# dp[1] = 10 20, 10 30, 10 50 / 20 30, 20 50 / 30 50
# dp[2] = 10 20 30, 10 20 50, 10 30 50


# 부분수열 1개
# 2개
# 3개 
# 4개

N = int(input())
arr = [0] + list(map(int, input().split()))
#dp = [-1] * (N + 1)
dp = [-1 for _ in range(N + 1)]

# 초기값 처리
dp[1] = 1

# DP Table 갱신
for n in range(2, N + 1): # dp[n]
    best = 0
    for i in range(1, n):
        if arr[n] > arr[i]:
            best = max(best, dp[i])
    dp[n] = best + 1

print(max(dp[1:]))





