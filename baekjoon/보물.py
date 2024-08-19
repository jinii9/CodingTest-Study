# S의 최솟값 출력
# 브루트
# N = 50
# 50 ^ 50

# 그리디
# 1 2 3 7 8
# 6 1 1 1 0
# 6 2 3 7

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

B = sorted(B)
A = sorted(A, reverse=True)

answer = 0
for i in range(N):
    answer += A[i] * B[i]

print(answer)