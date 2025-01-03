# NxM
# 1 이동, 0 이동X
# (1,1)에서 출발, (N, M) 위치로 이동 -> 최소 이동 칸
# 칸을 셀 때 시작 위치, 도착 위치도 포함

# 최소 거리 -> bfs

from collections import deque

def bfs(y, x):
	global maze, N, M
	# _maze = maze
	maze = [list(map(int, row)) for row in maze]

	dx = [-1, 1, 0, 0]
	dy = [0, 0, -1, 1]

	q = deque()
	q.append((y, x))
	maze[y][x] = 1
	
	while q:
		y, x = q.popleft()
		for i in range(4):
			ny = y + dy[i]
			nx = x + dx[i]

			if nx < 0 or ny < 0 or nx >= M or ny >= N:
				continue
			
			if int(maze[ny][nx]) == 1:
				q.append((ny, nx))
				maze[ny][nx] = maze[y][x] + 1


	return maze[N-1][M-1]


N, M = map(int, input().split()) # y, x
maze = [input() for _ in range(N)]

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# answer = 0
# for y in range(N):
# 	for x in range(M):
# 		answer(min(answer, bfs(y, x)))
answer = bfs(0, 0)

print(answer)




# 1이 존재한다 = 간선이 존재한다
# 가중그래프가 아닌 그래프가 아닌 경우의 최단경로는 -> BFS