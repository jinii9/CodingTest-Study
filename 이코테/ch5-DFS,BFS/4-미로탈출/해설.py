from collections import deque

n,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

print(graph)
# 상 하 좌 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    # 큐 빌 때까지 반복whi
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 찾기 공간 벗어난 경우 무시
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1 ### 이 부분이 중요!
                queue.append((nx, ny))

    print(graph)
    return graph[n-1][m-1]



print(bfs(0,0))

# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111