# 40m

# 활성화 / 비활성화
# Ai는 각각 mi 바이트만큼의 메모리를 사용
# 비활성화 후 다시 실행 비용 : Ci
# 새로운 앱 B 실행 -> M 바이트 이상의 메모리 추가 확보 필요
# 현재 활성화 되어 있는 앱들 중에서 몇 개를 비활성화 하여 M 바이트 이상의 메모리를 추가로 확보해야 하는 것
# 비활성화 했을 경우 비용 ci의 합을 최소화 하여 필요 메모리 M 바이트 확보할 것

# [입력값]
# N(활성화된 앱 개수) M(필요한 메모리 바이트)
# 활성화 되어 있는 앱이 사용중인 메모리 mN
# 비활성화 했을 경우의 비용 cN

# 5 60
# 30 10 20 35 40
# 3 0 3 5 4

# 브루트포스
# 1. 60이 되는 앱 조합 구하기
# 2. 조합마다 비용 구하기
# 3. 비용 min
# 시간복잡도 : 2^N*N = 2^100 

# DP
# 메모리는 클수록 좋다.
# N M C
# dp[n][m] : 앱 N개까지 보고 M바이트를 얻기 위한 최소 비용
## dp테이블 크기 : 100 * 10,000,000 = 1,000,000,000
# dp[n][c] : 앱 N개까지 보고 C비용을 가지는 최대? 메모리 바이트
## dp테이블 크기 : 100 * (100*100) = 굿

# dp[n][c] = max(dp[n-1][c], dp[n-1][c-Cn]+Mn)

N, M = map(int, input().split())
mems = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))

INF = int(1e12)
dp= [[0]*10001 for _ in range(N+1)] 

for n in range(1, N+1):
    for c in range(10001):
        dp[n][c] = dp[n-1][c]
        if c - costs[n] >= 0:
            dp[n][c] = max(dp[n-1][c], dp[n-1][c-costs[n]] + mems[n])

answer = INF
for c in range(10001):
    if dp[N][c] >= M:
        answer = min(answer, c)

print(answer)