# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())
# n, m = map(int, '3 3'.split())
# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input()))) # [[0, 0, 1], [0, 1, 0], [1, 0, 1]]

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    print('(', x, y, ')')
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        print('!!(',x,y,')')

        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y) # 상
        dfs(x + 1, y) # 하
        dfs(x, y - 1) # 좌
        dfs(x, y + 1) # 우
        return True

    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result) # 정답 출력

############################################################
# return True 발생 경우
# 1. 현재 노드가 방문하지 않은 노드(0)일 때.
# 2. 현재 노드를 방문 처리하고(1로 변경), 상하좌우 인접한 노드에 대해 dfs를 재귀적으로 호출하여, 연결된 모든 노드를 방문 처리한 후.
# 이 과정을 통해 하나의 연결된 구역을 완전히 탐색하게 되고, 이 때 처음 방문한 노드에서 return True를 하여, 해당 구역의 탐색이 성공적으로 완료되었음을 나타냄.
