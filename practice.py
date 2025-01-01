# 57~

# 길이 N 수열
# 연속된 수들의 부분합 >= S 중에서 가장 짧은 길이 구하기

# 브루트포스
# 부분 -> 시작점, 끝점 고르기
# N * NC2 = 100000000 = 1억
# 이분탐색 or 투포인터

# 이분탐색(파라매트릭)
# 기준 - S 이상 되는 것 : FFFTT..
# left, right 고르면서 S 이상이 되는 것만 pick하기
# right 고를 때 이분탐색 : 가장 오른쪽 F 구하고, +1

def parametric_search(left):
    global N, S, psum

    # cur = -1
    cur = left - 1
    step = N

    while step!=0:
        while (cur + step <= N) and (psum[cur + step] - psum[left - 1] < S): # 연속된 수들의 부분합이 S보다 작을 때(이때 누적합이 필요한 것이다)
            cur += step
        step //= 2
    
    return (cur + 1) # 첫 True 값


N, S = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# 누적합
psum = [0] * (N + 1)
for i in range(1, N+1):
	psum[i] = psum[i-1] + arr[i]

answer = int(1e6)
for left in range(1, N+1):
    right = parametric_search(left)

    if right <= N: # 합 S가 없을 경우 가드
      answer = min(answer, right - left + 1)

print(answer if answer != int(1e6) else 0)