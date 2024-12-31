# N개의 수로 된 수열
# 연속된 부분수열 중에서 합이 M이 되는 경우의 수

# 연속된 부분수열 구하는 방법
# 조합 P X


# # <시작지점을 고정하고 모든 끝점의 후보를 살펴보기>
# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
# answer = 0

# for i in range(N): # 시작하는 부분수열 : left
# 	sum = 0
# 	for j in range(i, len(arr)): # right
# 		sum += arr[j]
# 		if sum == M:
# 			answer += 1


# print(answer)


## <누적합> : 배열의 첫번째 원소부터 각 위치까지의 합을 저장한 것
# 구간의 합을 O(1)로 구할 수 있다

# input
N, M = map(int, input().split())
arr = [0] + list(map(int, input().split())) # 인덱스 1부터 시작하도록 0 추가

# solve
psum = [0] * (N + 1)

for i in range(1, N + 1):
    psum[i] = psum[i - 1] + arr[i] # 누적합 미리 계산
# psum = [0, 1, 2, 3, 4]

ans = 0
for left in range(1, N + 1):
    for right in range(left, N + 1):
        cur_sum = psum[right] - psum[left - 1] # 구간 합
		# psum[left-1] : left 바로 전까지의 누적합
        if cur_sum == M:
            ans += 1

print(ans)




