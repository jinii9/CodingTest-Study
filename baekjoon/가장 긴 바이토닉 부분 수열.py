# 1 5 2 1 4 3 4 5 2 1

N = int(input())
arr = list(map(int, input().split()))

dp1 = [0] * N
dp2 = [0] * N

# dp1
for n in range(0, N):
    best = 0
    for i in range(0, n):
        if arr[n] > arr[i]:
            best = max(best, dp1[i])
    dp1[n] = best + 1

# dp2
for n in range(N-1, -1, -1):
    dp2[n] = 1
    for i in range(N-1, n, -1):
        if arr[n] > arr[i]:
            dp2[n] = max(dp2[n], dp2[i] + 1)

answer = 0
for i in range(N):
    answer = max(answer, dp1[i] + dp2[i] - 1)

print(answer)

