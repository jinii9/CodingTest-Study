def is_possible(y, x, num):
    # 가로
    for col in range(9):
        if matrix[y][col] == num:
            return False
    # 세로
    for row in range(9):
        if matrix[row][x] == num:
            return False

    # 3x3
    for row in range(3):
        for col in range(3):
            if matrix[3*(y//3) + row][3*(x//3) + col] == num:
                return False
    
    return True


def search(depth):
    global matrix, pos
    # base
    if depth == len(pos):
        for i in range(9):
            for j in range(9):
                print(matrix[i][j], end=' ')
            print()
        exit(0)
        return

    y, x = pos[depth]

    # recursive
    for num in range(1, 10):
        if is_possible(y, x, num):
            matrix[y][x] = num
            search(depth + 1)
            matrix[y][x] = 0


# input
matrix = [list(map(int, input().split())) for _ in range(9)]

pos = [] # board의 0인 자리 모음

for i in range(9):
    for j in range(9):
        if matrix[i][j] == 0:
            pos.append((i,j))

search(0)
