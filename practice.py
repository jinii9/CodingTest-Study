# N개의 수 1차원 배열
# 이 배열을 M개 이하의 구간으로 나누기 
# -> 구간의 점수의 최대값을 최소로
# 구간의 점수 : 최대값 - 최소값
# 연속된 수

# solution
# 최댓값의 최솟값 -> 파라매트릭서치(답의 후보 k)
# FFFFFTT..
# 구간의 점수의 최대값이 k 이하일 때 가능한가?
#


import sys
input = lambda: sys.stdin.readline().strip()


# 1 5 4 5 2 1 3 7
def is_possible(k): # 구간의 점수의 최대값이 k 이하가 가능하면 return True
    global N, M, arr
	
    count = 0
    max_value = arr[0]
    min_value = arr[0]

    # 구간의 점수의 최대값 구하기
    for index in range(1, N): # 배열 돌기
        max_value = max(max_value, arr[index])
        min_value = min(min_value, arr[index])
        if (max_value - min_value) > k: # k 초과하는 순간에 구간 넣기             
            count += 1
            max_value = arr[index]
            min_value = arr[index]

    count += 1 # 마지막 구간은 카운트가 안되므로 따로 처리해주기

    return (count <= M)

		
N, M = map(int, input().split()) # 배열의 크기, 구간 수
arr = list(map(int, input().split()))

# 파라매트릭
cur = -1
step = 10000 # 구간의 점수 최댓값

while step != 0:
	while cur + step < 10001 and not is_possible(cur + step): # false가 나오는 곳에서
		cur += step
	step //= 2

print(cur + 1) # 가장 처음 나오는 True 위치

# 피리매트릭 서치 코드는 가장 오른쪽의 값을 구하는 문제
# 우리는 최소값 True 부분을 구해야하므로
# False의 맨 오른쪽으로 구하고, +1 하면 된다.