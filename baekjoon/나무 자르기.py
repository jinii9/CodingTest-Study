# 나무 M미터
# 높이 H미터

# 20 15 10 17 -> 높이 15
# 15 15 10 15

# M미터의 나무 가져가기 위한 절단기 높이H 최댓값

# N 나무의 수
# M 가져갈 나무의 길이

# solve
# 브루트포스 X
# 최댓값 -> DP, 파라매트릭
# 15를 기준으로 T,F -> 파라매트릭


# 파라매트릭
# 절단기의 높이 H 최댓값 구하기
# step은 탐색할 범위이다 -> 배열의 길이가 아니라 높이의 최댓값까지 탐색해야 한다!!!
# 1e9 = 1,000,000,000 (10의 9승)


# 높이를 k로 잡있을 때 M개 이상을 반환할 수 있는지 없는지
def is_possible(k):
	global N, M, heights

	count = 0
	for h in heights: # 20 15 10 17
		if k < h:
			count += (h - k)
	
	if count >= M:
		return True
	
	return False

def parametric_search(): # heights
	cur = -1
	step = int(1e9) + 1 # 탐색할 범위

	while step != 0:
		# (arr[cur+step] <= True)
		while (cur + step <= int(1e9)) and is_possible(cur + step):
			cur += step		
		step //= 2		
	
	return cur

N, M = map(int, input().split())
# heights = [map(int, input().split()) for _ in range(N)]
heights = list(map(int, input().split())) # 한줄의 입력만 받을 때는 이렇게 할 것


print(parametric_search())
