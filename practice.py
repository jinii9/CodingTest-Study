# 25~

# 한 컴퓨터가 바이러스 걸리면, 그 컴퓨터와 연결된 컴퓨터 모두 바이러스 전염
# 1번 컴퓨터 바이러스 걸림 -> 바이러스 걸린 컴퓨터 수 출력

from collections import deque
# bfs
def bfs():
    global network
    count = 0

    q = deque()
    q.append(1)
    visited[1] = True
	
    while q:
        node = q.popleft()
        for adj_node in network[node]:
             if not visited[adj_node]:
                  q.append(adj_node)
                  visited[adj_node] = True
                  count += 1
             
    return count
	

com_count = int(input()) # 컴퓨터 수
edge_count = int(input()) # 간선 수

# network = [] * (edge_count+1)
network = [[] for _ in range(com_count + 1)]
for _ in range(edge_count):
	a, b = map(int, input().split())
	network[a].append(b)
	network[b].append(a) # 양방향 그래프

visited = [False] * (com_count + 1)

print(bfs())