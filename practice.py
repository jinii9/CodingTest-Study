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
    x, y = 0, 0  # 현재 위치
    directions = []

    # start 지점
    for i, iVal in enumerate(park):
        for j, jVal in enumerate(iVal):
            if jVal == "S":
                x = i
                y = j

    # 방향에 따른 좌표 변화량 설정
    direction_delta = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}

    # routes 해석
    for route in routes:
        direction, distance = route.split()
        distance = int(distance)
        tempX, tempY = x, y  # 초기 위치 저장!!!

        # 단계별 이동 필수!!
        for _ in range(distance):
            nx = x + direction_delta[direction][0]
            ny = y + direction_delta[direction][1]

            if nx < 0 or nx >= len(park) or ny < 0 or ny >= len(park[0]):
                x, y = tempX, tempY
                break
            if park[nx][ny] == "X":
                x, y = tempX, tempY
                break
            x, y = nx, ny

    return [x, y]

# '남쪽으로 2칸 이동할 때 장애물이 있는 칸을 지나기 때문에' 이 문구를 확인하지 못함. -> 예시 보기 귀찮아도 잘 살펴볼 것!
# 그래서 단계별로 모두 확인해야 하는 것을 빼먹고 코드를 작성하여 재작성..

# 유의점
# 단계별로 하기 위해서는 한번에 x, y값을 받아오면 안되고 for문 돌면서 탐색 들어가야 함
# ex) 남 2 -> (+2, 0)을 저장해서 바로 계산하는게 아니라, 딕셔너리 값을 1씩 지정해두고 for문을 2번 돌아야 하는 것!!!
