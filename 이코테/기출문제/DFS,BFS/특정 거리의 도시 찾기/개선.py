from collections import deque

n, m, k, x = map(int, input().split()) # 4 4 2 1
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# bfs
def bfs(graph, start):
    distance = [-1] * (n + 1)
    distance[start] = 0

    queue = deque([start])
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not distance[i] == -1: # 방문 안했을 시에
                distance[i] = distance[v] + 1
                queue.append(i)

    return distance


distance = bfs(graph, x)

result = []
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)

##################################
# 굳이 visted 배열을 따로 선언하지 않고, distance 배열의 초기 값을 -1로 하여, -1일 시 방문 X한 걸로 판단
# distance 배열 자체는 정렬되어 있지 않지만, 도시 번호(i)에 대해 1부터 n까지 순차적으로 탐색하기 때문에, 결과적으로 도시 번호가 오름차순으로 출력된다. 따라서 따로 sort() 함수 사용 안해도 됨.



