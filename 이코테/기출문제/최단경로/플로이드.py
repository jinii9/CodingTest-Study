# 최단 거리
# 플로이드 워셜
# 입력
INF = int(1e9)

n = int(input()) # 도시 = 노드
m = int(input()) # 버스 = 간선

graph =[[INF] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    a, b, cost = map(int, input().split())
    if cost < graph[a][b]: # 문제의 조건 삽입
        graph[a][b] = cost

# 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 로직
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print(0, end=' ')
        else:
            print(graph[a][b], end=' ')
    print()

# 5
# 14
# 1 2 2
# 1 3 3
# 1 4 1
# 1 5 10
# 2 4 2
# 3 4 1
# 3 5 1
# 4 5 3
# 3 5 10
# 3 1 8
# 1 4 2
# 5 1 7
# 3 4 2
# 5 2 4







