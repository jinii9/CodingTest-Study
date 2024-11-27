# 세로 R, 가로 C
# 상하좌우 -> 다른 알파벳
# 최대 몇 칸

# 브루트포스
# dp X : 최대길이 값 뿐만 아니라 모든 경로의 알파벳 값 필요
# 그리디 X
# 백트래킹

def search(y, x):
    global R, C, board, answer, dy, dx, cur_len

    if y < 0 or y >= R or x < 0 or x >= C:
        return
    if check[ord(board[y][x]) - ord('A')]: # 알파벳 방문 여부 체크
        return
    
    check[ord(board[y][x]) - ord('A')] = True
    cur_len += 1
    answer = max(answer, cur_len)

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        search(ny, nx)

    # 백트래킹
    check[ord(board[y][x]) - ord('A')] = False
    cur_len -= 1


R, C = map(int, input().split())
board = [input() for _ in range(R)]

check = [False] * 26 # 알파벳 총 26개
cur_len = 0 # 방문한 알파벳 개수
answer = 0

# 상 하 좌 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

search(0, 0)
print(answer)



                

