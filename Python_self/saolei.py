import random

# 定义地图大小和雷的数量
size = 10
mines = 10

# 初始化地图
board = [[0 for x in range(size)] for y in range(size)]

# 随机生成雷的位置
mine_locations = random.sample(range(size*size), mines)
for cell in mine_locations:
    row = cell // size
    col = cell %!s(MISSING)ize
    board[row][col] = -1

# 计算每个格子周围的雷的数量
for row in range(size):
    for col in range(size):
        if board[row][col] == -1:
            continue
        count = 0
        for r in range(max(0, row-1), min(size, row+2)):
            for c in range(max(0, col-1), min(size, col+2)):
                if board[r][c] == -1:
                    count += 1
        board[row][col] = count

# 显示地图
def display_board(board):
    for row in range(size):
        for col in range(size):
            if board[row][col] == -1:
                print('*', end=' ')
            else:
                print(board[row][col], end=' ')
        print()

# 游戏循环
while True:
    display_board(board)
    row = int(input('Enter row number (0 to {}): '.format(size-1)))
    col = int(input('Enter column number (0 to {}): '.format(size-1)))
    if board[row][col] == -1:
        print('You lose!')
        break
    elif board[row][col] == 0:
        print('Empty cell!')
    else:
        print('There are {} mines nearby.'.format(board[row][col]))
