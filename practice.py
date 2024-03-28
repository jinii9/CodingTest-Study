2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2

# 로직
def solution(row, col):# 3 4
    for a in range(1, row + 1): # 행
        for b in range(2, col + 1): # 열
            if a == 1:
                dp[a][b] = max(dp[a][b-1], dp[a+1][b-1]) + dp[a][b]
            elif a == 2:
                dp[a][b] = max(dp[a-1][b-1], dp[a][b-1], dp[a+1][b-1]) + dp[a][b]
            elif a == 3:
                dp[a][b] = max(dp[a-1][b-1], dp[a][b-1]) + dp[a][b]

# 입력
T = int(input())

dp = []
for _ in range(T):
    n, m = map(int, input().split())
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    arr = list(map(int, input().split()))
    i = 0
    for a in range(1, n + 1):
        for b in range(1, m + 1):
            dp[a][b] = arr[i]
            i += 1

    print(dp)
    solution(n, m)
    # print("답:", dp[n][m])
    print("답:", max(dp[a][m] for a in range(1, n+1)))

