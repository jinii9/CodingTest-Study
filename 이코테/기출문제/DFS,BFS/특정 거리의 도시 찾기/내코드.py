## ~45
from collections import deque

# n 도시의 개수
# m 도로의 개수
# k 최단거리 정보
# x 출발 도시의 번호

# 입력
# 4 4 2 1
# 1 2
# 1 3
# 2 3
# 2 4
n, m, k, x = map(int, input().split()) # 4 4 2 1
graph = [[] for _ in range(m + 1)]
for _ in range(m):
    # graph.append(list(map(int, input().split()))) # [[1, 2], [1, 3], [2, 3], [2, 4]]
    a, b = map(int, input().split())
    graph[a].append(b)

print(graph)

# bfs
def bfs(graph, start):
    distance = [0] * (n + 1)
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print("v:", v)
        for i in graph[v]:
            print("i:", i)
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                # distance[i] += 1
                distance[i] = distance[v] + 1
                # distance[v] += distance[i]

    return distance


visited = [False] * (n + 1)
distance = bfs(graph, x)
print(distance)

result = []
for i in range(len(distance)):
    if distance[i] == k:
        result.append(i)

result.sort()
if result:
    for i in range(len(result)):
        print(result[i])
else:
    print(-1)

############################################
# '모든 도로의 거리는 1'이라는 조건 덕분에 bfs 이용하여 간단 해결 가능한 것!!!

# [수정 필요]
## graph 배열 선언 시, range를 'm+1'이 아니라 'n+1'로 할당해야 한다. <- 배열의 인덱스가 도시를 나타내기 때문에

# [review]
## 1. graph 배열 input 방법
### 처음에는 graph 배열에 [[1, 2], [1, 3], [2, 3], [2, 4]]와 같이 넣었다.
### 그러나 계속 생각해보니, 인덱스를 도시 번호로 하여 진행해야 한다고 깨달았다. => [[], [2, 3], [3, 4], [], []]

## 2. distance 배열 로직 방법
### 처음에는 'distance[i] += 1'로 로직을 구성했다.
### 그러나 그렇게 하니 전에 있던 거리 값이 update가 되지 못했다. => distance[i] = distance[v] + 1


