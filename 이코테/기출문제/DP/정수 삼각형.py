# 왼쪽 위 / 왼쪽 위, 위 / 위
# 점화식 : dp[i][j] = arr[i][j] + max(dp[i-1][j-1], dp[i-1],j)
n = int(input())
dp = []
for i in range(n):
    dp.append(list(map(int,input().split())))

print(dp)

#
for i in range(1, n):
    for j in range(len(dp[i])):
        # 바로 위에서 내려올 때
        if j == 0:
            dp[i][j] += dp[i-1][j]
        # 왼쪽 위에서 내려올 떄
        elif j == len(dp[i])-1:
            dp[i][j] += dp[i-1][j-1]
        # (중앙)왼쪽 위, 바로 위에서
        else:
            dp[i][j] += max(dp[i-1][j], dp[i-1][j-1])

print(dp)
print(max(dp[n-1]))

# 5  
# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5
#####################################
# !!삼각형으로 생각하지 말고, 입력값 모양으로 생각하기
## [before]
# 왼쪽 끝 [i - 1][j + 1]
# 중앙 [i - 1][j + 1], [i-1][j - 1]
# 오른쪽 끝 [i-1][j - 1]
## [after]
## 왼쪽 위 / 왼쪽 위, 위 / 위

# !!꼭 if가 아니라 elif 사용할 것
