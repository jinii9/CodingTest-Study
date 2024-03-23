# 1번 - k번 - x번
# 1k + kx
# 플로이드워셜
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split()) # 회사, 경로 개수
graph = [[INF] * (n + 1) for i in range(n + 1)]

for a in range(n + 1):
    for b in range(n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1 ## 빼먹지 말 것!

x, k = map(int, input().split())

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x] ## 1번 회사에서 k번 회사까지의 거리와 k번 회사에서 x번 회사까지의 거리를 더한 값

if distance >= INF:
    print("-1")
else:
    print(distance)

##################################################
# 다익스트라 알고리즘으로 풀지 않는 이유 (다익스트라 알고리즘을 2번 실행해야 함!)
## 1. 1번~k번 최단경로 찾기
## 2. k번~x번 최단경로 찾기
## 3. 두 경로의 길이 합산