# 회문: 앞뒤방향으로 볼때 같은 순서
# 유사회문: 한문자 삭제하여 회문 만들 수 있다.
# 회문 0, 유사회문 1, 일반문자열 판단 2

# solve
# 브루트포스
# T30 * 100,000*100,000
# 이진탐색 or 투포인터

# 투포인터
# left, right 양 사이드에서 시작
# 
# 7, 7//2= 3 
# 6, 6//2= 3 
import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 늘리기

def recursion(value, left, right, count):
	global T
	# base
	if count > 1:
		return 2
	# if left == right and count==1:
	# 	return 1
	if left >= right:
		# return 0
		return count
	
	# recursive
	if value[left] == value[right]:
		return recursion(value, left+1, right-1, count)

	else:
		# 1. right를 옮겨보기
		skip_right = recursion(value, left, right-1, count+1)
		# count -=1 # 백트래킹
		if skip_right == 1:
			return 1
		# 2. left를 옮겨보기
		# recursion(value, left+1, right, count+1)
		# count-=1
		skip_left = recursion(value, left+1, right, count+1)
		if skip_left == 1:
			return 1
		return 2
	
	# return 2



T = int(input()) # 문자열 개수
arr = [input() for _ in range(T)]

for value in arr:
	left = 0
	right = len(value)-1
	# for left in range(T):
	print(recursion(value, left, right, 0))
		
		