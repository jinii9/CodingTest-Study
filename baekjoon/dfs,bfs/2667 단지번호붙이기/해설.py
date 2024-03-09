# 상하좌우 이동
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    global count # 함수 내부에서 값 변경 시, 함수 외부의 count 값에도 반영되도록 전역 변수로 선언!
    # visited[x][y] = True
    maps[x][y] = 0
    count += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and maps[nx][ny] == 1:
            dfs(nx, ny)

# 입력
n = int(input())
maps = [list(map(int, input())) for _ in range(n)] # graph
# visited = [[False] * n for _ in range(n)] # 방문 여부 판단 2차원 리스트
result = []

for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            count = 0
            dfs(i, j)
            result.append(count)

print(len(result))
for i in sorted(result):
    print(i)
