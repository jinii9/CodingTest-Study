# 도현이의 집 N개
# 공유기 C개
# 가장 인접한 두 공유기 사이의 거리를 가능한 크게

# 최솟값의 최대값 -> 파라매트릭서치
# TTTTFFF..
# 1. 모든 경우 살펴보기
# 2. 답의 후보 모두 살펴보기 : 거리 k가 될 수 있는지


import sys
input = lambda: sys.stdin.readline().rstrip()

def is_possible(k):
	global N, C, distances

	before_index = 0
	cnt = 1 # 공유기 C개 설치 확인용 : 처음에 설치하는게 무조건 이득(1)
	for index in range(1, N): # 도현이 집들을 돌면서
		if distances[index] - distances[before_index] >= k:
			before_index = index
			cnt += 1

	return cnt >= C


N, C = map(int, input().split())
distances = sorted([int(input()) for _ in range(N)]) # 집의 좌표

# parametric search
cur = -1
step = int(1e9) + 1

while step != 0:
	while cur + step <= int(1e9) and is_possible(cur + step):
		cur += step
	step //= 2

print(cur)

