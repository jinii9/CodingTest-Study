# MxN
# 8x8 체스판
# 맨 왼쪽 위 칸이 흰색인 경우 or 검은색인 경우

# 2*NM*64


def get_min(sy, sx):
    global baord, chess1, chess2
    case1 = case2 = 0
    
    for i in range(8):
        for j in range(8):
            case1 += (board[sy+i][sx+j] != chess1[i][j])
            case2 += (board[sy+i][sx+j] != chess2[i][j])
    
    return min(case1, case2)


chess1 = [['' for _ in range(8)] for _ in range(8)] # 맨 위쪽 위 칸이 흰색인 경우
chess2 = [['' for _ in range(8)] for _ in range(8)] # 검은색인 경우

for i in range(8):
    for j in range(8):
        chess1[i][j] = ('W' if (i+j)%2==0 else 'B')
        chess2[i][j] = ('B' if (i+j)%2==0 else 'W')

N, M = map(int, input().split())
board = [input() for _ in range(N)]

best = int(1e9)
for sy in range(N):
    for sx in range(M):
        if sy+7 >= N or sx+7 >= M:
            continue
        best = min(best, get_min(sy,sx))

print(best)