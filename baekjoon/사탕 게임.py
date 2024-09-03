# NxN
# 사탕의 색이 다른 인접한 두 칸 교환
# 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 or 열)
# C P Z Y

# 1. 상하좌우로 사탕의 색이 다른지 체크
# 2. 다르다면 교환
# 3. 가장 긴 연속 부분 고르기

def get_max(y, x):
    global N, matrix
    best = 0

    # 열 col
    cnt = 0
    bef = '-'
    for i in range(N):
        if bef == matrix[i][y]:
            cnt += 1
        else:
            cnt = 1
        bef = matrix[i][y]
        best = max(best, cnt)
    
    # 행 row
    
        
    # 행 row
    
    # # 열 col
    # for i in range(N):
    #     cnt = 0
    #     bef = '-'
    #     for j in range(N):
    #         if bef == matrix[i][j]:
    #             cnt += 1
    #         else:
    #             cnt = 1
    #         bef = matrix[i][j]
    #         best = max(best, cnt)

    # # 행 row
    # for i in range(N):
    #     cnt = 0
    #     bef = '-'
    #     for j in range(N):
    #         if bef == matrix[j][i]:
    #             cnt += 1
    #         else:
    #             cnt = 1
    #         bef = matrix[j][i]
    #         best = max(best, cnt)
    
    return best


N = int(input())
# matrix = [input().split() for _ in range(N)]
# matrix = [input() for _ in range(N)]
matrix = [list(input()) for _ in range(N)]
# print(matrix)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
answer = 0

# 모든 matrix 돌기
for y in range(N):
    for x in range(N):
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny >= N or ny < 0 or nx >= N or nx < 0:
                continue

            # 사탕 색 체크 : 다를 경우 함수 돌리기
            if matrix[y][x] != matrix[ny][nx]:
                matrix[y][x], matrix[ny][nx] = matrix[ny][nx], matrix[y][x]
                # answer = max(answer, get_max())
                answer = max(answer, get_max(ny, nx))
                matrix[y][x], matrix[ny][nx] = matrix[ny][nx], matrix[y][x]

print(answer)
