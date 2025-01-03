# 1~N
# 정점의 개수 N
# 간선의 개수 M
# 탐색 시작 정점 번호 V
# 양방향

# 정점 번호가 작은 것을 먼저 방문

from collections import deque
def dfs(node):
	global adj_list, visited

	# base
	if visited[node]:
		return	

	visited[node] = True
	print(node, end=' ')

	# recursive
	for adj_node in sorted(adj_list[node]):
		dfs(adj_node)

def bfs():
	global adj_list, visited, V

	q = deque()
	q.append(V)
	visited[V] = True

	while q:
		node = q.popleft()
		print(node, end=' ')

		for adj_node in sorted(adj_list[node]):
			if not visited[adj_node]:
				q.append(adj_node)
				visited[adj_node] = True


N, M, V = map(int, input().split())

adj_list = [[] for _ in range(N+1)]
for _ in range(M):
	a, b = map(int, input().split())
	adj_list[a].append(b)
	adj_list[b].append(a)

visited = [False] * (N+1)
dfs(V)
print()

visited = [False] * (N+1)
bfs()
print()
