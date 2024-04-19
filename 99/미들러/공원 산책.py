# 40 ~
# 지나다니는 길 O / 장애물 X
# E 5 : 동쪽 5칸 이동
# 공원 문자열 배열 park
# 로봇 강아지가 수행할 명령 배열 routes / 이동할 방향, 칸 수

# N 북 : -x
# S 남 : + x
# W 서 : - y
# E 동 : + y
def solution(park, routes):
    answer = []
    x, y = 0, 0
    directions = []

    # start 지점
    for i, iVal in enumerate(park):
        for j, jVal in enumerate(iVal):
            if jVal == "S":
                x = i
                y = j

    # routes 해석
    for route in routes:
        direction, dist = route.split()
        dx, dy = 0, 0  # 이동 값

        if direction == "N":
            dx -= int(dist)
        elif direction == "S":
            dx += int(dist)
        elif direction == "W":
            dy -= int(dist)
        elif direction == "E":
            dy += int(dist)

        x += dx
        y += dy
        # 이동
        if x >= len(park) or y >= len(park[0]) or park[x][y] == 'X':
            x -= dx
            y -= dy

    return [x, y]