# ~30

# 1칸 또는 2칸

# 4칸
# 1 1 1 1
# 1 2 1
# 1 1 2
# 2 1 1
# 2 2

# 3칸
# 2 1
# 1 2
# 1 1 1

# dp

def solution(n):
    dp = [0] * 2001
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567

    answer = dp[n]
    print(answer)
    return answer
