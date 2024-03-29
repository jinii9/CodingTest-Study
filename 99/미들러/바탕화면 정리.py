# 빈칸은 ".", 파일이 있는 칸은 "#"
# 최소한의 이동거리
# 점 S와 점 E를 각각 드래그의 시작점, 끝점
# "드래그 한 거리"는 |rdx - lux| + |rdy - luy|
# 왼쪽 위, 오른쪽 아래로 하는 직사각형 내부에 있는 모든 파일이 선택

def solution(wallpaper):
    # print(wallpaper)
    INF = int(1e9)
    min_x, min_y, max_x, max_y = INF, INF, -1, -1  # lux, luy, rdx, rdy

    for i in range(len(wallpaper)):  # 행
        for j in range(len(wallpaper[i])):  # 열
            if wallpaper[i][j] == '#':  # wallpaper[i][j]
                print(i, j)
                min_x = min(min_x, i)
                min_y = min(min_y, j)
                max_x = max(max_x, i)
                max_y = max(max_y, j)

    print([min_x, min_y, max_x, max_y])
    return [min_x, min_y, max_x + 1, max_y + 1]

##################################################
# 처음에는 '최단거리' 문제라고 생각하고 bfs 문제인가 하고, wallpaper문자열을 0과 1로 표현해서 그래프로 나타내기 위해서 애를 엄청 먹었었다. (진짜 헛질 작렬;;)
# 근데 생각해보면 BFS는 최단 거리 순으로 탐색할 때 사용하지만, 이 문제는 격자판에서 최소한의 드래그 거리를 찾는 문제이다. => 격자판 상의 # 위치를 파악해서 "경계"를 찾는 거에 초점을 두어야 하는 것!
# 그래서 # 위치에 있는 최소 좌표의 값과 최대 좌표의 값을 찾으면 되는 것!!!
# 대신에 return해줄 때 드래그의 끝점을 나타내야 하므로 최대 좌표의 값에 +1씩 해준다!
