# N : 수민이 위치
# K : 동생 위치
# 수빈이의 위치 X일 때 
# 걸으면 1초 후, X-1 or X+1
# 순간이동 하면 1초 후, 2*X

# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후일까

# 브루트포스
# 2^10만

# dp
# X-1, X+1, 2*X
# 5 6 7 8 9 10 11 122 13
# dp[n] : n까지 거리의 최소 시간
# X : dp[n] = min(dp[n-1], dp[n+1], dp[n//2])
# O : dp[i] = min(
#     dp[i-1] + 1,     // 한 칸 전진
#     dp[i/2] + 1,     // 순간이동 (i가 짝수일 때만)
#     dp[i+1] + 1
# )
# dp[i+1]을 사용하려면 미래의 값을 알아야 하는데, DP의 기본 원칙 X. dp[i]는 이전의 값들로만 계산되어야 한다.

# 가장 빠른 경로..시간? 구하기 -> BFS
# 위치 : 노드
# 간선 : 이동

from collections import deque

MAX = int(1e5) # 100,000
N, K = map(int, input().split())
# arr = [0] * (K+1)
visitied = [False] * (MAX+1)


q = deque()
q.append((0, N)) # (time:=거리, position)
visitied[N] = True

# dn = [-1, 1, 0]
while q:
	time, pos = q.popleft()

	if pos == K:
		print(time)
		exit()

	# for n in dn:
	for next_pos in [pos-1, pos+1, pos*2]:
		if (0 <= next_pos <= MAX) and (not visitied[next_pos]):
			q.append((time+1, next_pos))
			visitied[next_pos] = True



