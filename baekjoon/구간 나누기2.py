# 20~

# N개의 수 1차원 배열
# 이 배열을 M개 이하의 구간으로 나누기 
# -> 구간의 점수의 최댓값을 최소로
# 구간의 점수 : 최댓값 - 최솟값
# 연속된 수

# solution
# 최댓값의 최솟값 -> 파라매트릭서치
# 구간의 점수의 최댓값의 최솟값이 K가 될 수 있는가?
# k의 최솟값 찾기
# 구간의 점수가 k 이하인 경우
# T : k 이하
# F : k 초과

# 1. 정렬 X
# 2. is_possible 함수

# 1 5 4 5 2 1 3 7
# 1 5 | 4 5 2 1 3 7
def is_possible(k): # 구간의 점수가 k 이하인 경우 True
	global N, M, arr;

	# before_index = 0
	# count = 1 # 구간 C개 이하 설치 확인용
	max_value = arr[0]
	min_value = arr[0]
	# 구간의 점수 구하기
	for index in range(1, N): # 배열 반복문
		max_value = arr[index]

		# for c in range(count):
		# 	arr1 = arr[:before_index+1]
		# 	arr2 = arr[before_index:]

		# 	if max(max(arr1)-min(arr1),max(arr2)+min(arr2)) <= k:
		# 		count += 1
		# 		before_index = index

	
	return (count <= M)



N, M = int(input().split()) # 배열의 크기, 구간 수
arr = [int(input()) for _ in range(N)]

# 파라매트릭
cur = -1
step = 10000 # 구간의 점수 최댓값

while step != 0:
	while cur + step < 10001 and is_possible(cur + step):
		cur += step
	step //= 2

print(cur)