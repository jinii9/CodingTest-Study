# 25~

# 한 컴퓨터가 바이러스 걸리면, 그 컴퓨터와 연결된 컴퓨터 모두 바이러스 전염
# 1번 컴퓨터 바이러스 걸림 -> 바이러스 걸린 컴퓨터 수 출력

# dfs
def dfs(node):
	global network, visited

	# base
	if visited[node]:
		return 0
	
	visited[node] = True
	count = 1

	# recursive
	for cur_node in network[node]:
		count += dfs(cur_node)
	
	return count


com_count = int(input()) # 컴퓨터 수 = 노드
edge_count = int(input()) # 간선 수

# network = [] * (edge_count+1)
network = [[] for _ in range(com_count + 1)]
for _ in range(edge_count):
	a, b = map(int, input().split())
	network[a].append(b)
	network[b].append(a) # 양방향 그래프

visited = [False] * (com_count + 1)
print(dfs(1)-1)








# # <bfs 풀이>
# from collections import deque
# # bfs
# def bfs():
#     global network
#     count = 0

#     q = deque()
#     q.append(1)
#     visited[1] = True
	
#     while q:
#         node = q.popleft()
#         for adj_node in network[node]:
#              if not visited[adj_node]:
#                   q.append(adj_node)
#                   visited[adj_node] = True
#                   count += 1
             
#     return count
	

# com_count = int(input()) # 컴퓨터 수
# edge_count = int(input()) # 간선 수

# # network = [] * (edge_count+1)
# network = [[] for _ in range(com_count + 1)]
# for _ in range(edge_count):
# 	a, b = map(int, input().split())
# 	network[a].append(b)
# 	network[b].append(a) # 양방향 그래프

# visited = [False] * (com_count + 1)

# print(bfs())






# ##########################################
# # <dfs의 매개변수로 count를 넣는 경우>

# def dfs(node, count):
#     global network, visited

#     # base case: 이미 방문한 경우
#     if visited[node]:
#         return count  # 현재까지의 count 반환
    
#     visited[node] = True
#     count += 1  # 현재 노드를 포함한 전염된 수 증가

#     # recursive DFS 호출
#     for cur_node in network[node]:  # 현재 노드의 인접 노드
#         count = dfs(cur_node, count)  # 재귀 호출하여 전염된 수를 업데이트
    
#     return count

# com_count = int(input("컴퓨터 수를 입력하세요: "))  # 컴퓨터 수
# edge_count = int(input("간선 수를 입력하세요: "))  # 간선 수

# # 네트워크 초기화
# network = [[] for _ in range(com_count + 1)]  # 컴퓨터 수에 맞게 초기화
# for _ in range(edge_count):
#     a, b = map(int, input("간선을 입력하세요 (예: a b): ").split())
#     network[a].append(b)
#     network[b].append(a)  # 양방향 간선

# visited = [False] * (com_count + 1)  # 방문 여부 초기화
# result = dfs(1, 0) - 1  # 1번 컴퓨터는 제외
# print(result)
