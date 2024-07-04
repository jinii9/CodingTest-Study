# 1h

# 매초 번호가 낮은 종류의 바이러스부터 먼저 증식
# 이미 어떤 바이러스가 있다면, 그곳에는 다른 바이러스 들어갈 수 X
# S초가 지난 후에 (X,Y에 존재하는 바이러스의 종류 출력
# 존재 않는다면, 0 출력

# bfs 사용
# 숫자가 겹칠 경우 


from collections import deque

# 입력
N, K = map(int, input().split())
graph = []
data = [] # 바이러스가 있는 칸

for i in range(N):
    graph.append(list(map(int, input().split())))
    # 바이러스가 어디에 있는지 data에 저장
    for j in range(N):
        if graph[i][j] != 0:
            data.append(((i,j), graph[i][j], 0)) # 위치, 바이러스 값, 시간


input_S, input_X, input_Y = map(int, input().split())


# BFS

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0
queue = deque(data)

while queue:
    (x, y), value, s = queue.popleft()
    if s == input_S:
        answer = graph[input_X - 1][input_Y - 1]
        break

    for i in range(4):
        nx = x + dx[i]   
        ny = y + dy[i]
        
        if nx < 0 or ny < 0 or nx > N-1 or ny > N-1:
            continue

        if graph[nx][ny] != 0:
            if value < graph[nx][ny]: # 바이러스 작은 값이 뭔지 비교
                graph[nx][ny] = value
        else:
            graph[nx][ny] = value

        queue.append(((nx, ny), graph[nx][ny], s + 1))



print("answer:", answer)

##########################################################
# bfs 기초 코드만 잘 알고, 문제를 잘 풀이해보면 풀 수 있었던 문제!
# bfs 응용 문제라고 하더라도 겁 먹지 말고, bfs 기초 코드를 잘 생각해보자!

# 이 문제는 바이러스 입력 값을 받을 때, data 배열을 따로 만들어서, 바이러스 값이 있는 칸은 '따로' 저장하게 포인트~!

# 답지에서는 나처럼 바이러스의 최솟값이 뭔지 비교한게 아니라 애초에 처음에 data 배열을 sort 했다.
# 정렬하고 난 후에는 0일 경우에만 value 값을 업데이트하기 때문에, 바이러스가 겹칠(비교할) 일이 없다..!

# 3 3
# 1 0 2
# 0 0 0
# 3 0 0
# 2 3 2

# 3 3
# 1 0 2
# 0 0 0
# 3 0 0
# 1 2 2