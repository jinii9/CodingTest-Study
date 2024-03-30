# 30~
# 4 6
# 0 0 0 0 0 0
# 1 0 0 0 0 2
# 1 1 1 0 0 2
# 0 0 0 0 0 2

# dfs
# 벽의 개수 3개
# 0 빈칸, 1 벽, 2 바이러스
# 벽을 3개씩 세워가면서, 0의 최대 개수를 구해야 한다.

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

temp_graph = [[0] * m for _ in range(n)] # graph 변형 위해 원래 graph는 두고 복사할 temp_graph 선언
result = 0

def virus(x, y): # 바이러스 전염 함수
    for i in range(4): # 상하좌우 이동
        nx = x + dx[i]
        ny = y + dy[i]
        # 바이러스가 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp_graph[nx][ny] == 0:
                temp_graph[nx][ny] = 2 # 바이러스 전염
                virus(nx, ny)

def zero_count(): # 바이러스 전연 안된 0 구역 개수 세기 함수
    count = 0
    for i in range(n):
        for j in range(m):
            if temp_graph[i][j] == 0:
                count += 1
    return count

def dfs(count):
    global result # 함수 내에서 전역 변수의 값을 변경하려고 할 때는 해당 변수를 로컬 변수로 간주할 수 있기 때문에 -> global 키워드를 사용하여 해당 변수가 전역 변수임을 명시해야 하는 경우
    # 2. 울타리 3개가 설치되면 탐색 시작(바이러스 전염시키기)
    if count == 3:
        # 다음 단계에서 영향 미치면 안되게 때문에(복원 위해) 원래 graph는 두고, 새로운 배열 만들어서 복사해주기
        for i in range(n):
            for j in range(m):
                temp_graph[i][j] = graph[i][j]
        # 바이러스 찾기
        for i in range(n):
            for j in range(m):
                if temp_graph[i][j] == 2:
                    virus(i, j)
        # 0 개수
        result = max(result, zero_count())
        return # 빼먹지 말기!!!

    # 1. 울타리 설치
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1 # 울타리 설치
                count += 1
                dfs(count) # 다음 울타리 설치

                # (중요!!!) 백트래킹 : 다른 위치에 벽을 설치해보기 위해 돌아가기!
                graph[i][j] = 0
                count -= 1


dfs(0)
print(result)
##################################################################
# 처음에는 graph가 2인 상하좌우를 1로 벽을 세울 생각을 했다.