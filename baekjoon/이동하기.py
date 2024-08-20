# (1,1) ~ (N,M)
# 준규 위치 (1,1)
# (r, c) -> (r+1, c), (r, c+1), (r+1, c+1) = 아래, 오른쪽, 오른쪽 아래 대각선
# (r,c)~(N,M)까지의 사탕 개수의 최댓값

#  0 1 2
# 0
# 1
# 2


N, M = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

DP = [[0 for _ in range(M+1)] for _ in range(N+1)]


for i in range(1, N+1):
    for j in range(1, M+1):
        DP[i][j] += max(DP[i-1][j], DP[i][j-1], DP[i-1][j-1]) + graph[i-1][j-1]


print(DP[N][M])