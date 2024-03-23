# 3 2 1
# 1 2 4
# 1 3 2

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split()) # 도시, 통로, start
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for i in range(m):
    x, y, z = map(int, input().split()) # x~y. 메시지 전달 시간
    graph[x].append((y, z))

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start)) # 거리, 노드
    while q:
        dist, now = heapq.heappop(q) # 거리, 노드
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)

count = 0
# 도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
max_distance = 0
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)
# 시작 노드는 제외해야 하므로 count - 1을  출력
print(count - 1, max_distance)

# (오답)
# count = 0
# result = 0
# for i in range(1, n + 1):
#     if distance[i] != INF:
#         count += 1
#         result += distance[i]
# print(count, result)

###################################################
# 헷갈리지 말아야 할 점
## graph는 (b, c)가 append 된다 => (노드, 비용)
## q는 (dist, now)가 push 된다. => (비용, 노드)

# 오답
## '도시들이 모두 메시지를 받는 데까지 걸리는 시간'을 구해야하므로 최단거리 max 값을 구하면 됨!!
## 시작 노드 제외 필수!