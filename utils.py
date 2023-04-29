import random

# 시작, 도착 위치 랜덤 생성
def generate_start_goal(M, N, grid_world):
    while True:
        start = (random.randint(0, M - 1), random.randint(0, N - 1))
        end = (random.randint(0, M - 1), random.randint(0, N - 1))
        if start != end:
            break
    grid_world[start[0]][start[1]] = 'S'
    grid_world[end[0]][end[1]] = 'G'
    return start, end

# 장애물 초기화
def reset_obstacles(grid_world):
    for i in range(len(grid_world)):
        for j in range(len(grid_world[0])):
            if grid_world[i][j] == 'X':
                grid_world[i][j] = 'O'

def is_valid(new_x, new_y, cell_width, cell_height, grid_world):
    row, col = (new_y-100)//cell_height, (new_x-75)//cell_width
    return 75 <= new_x <= 675 and 100 <= new_y <= 700

def is_valid_drag(new_x, new_y, cell_width, cell_height, grid_world, start_goal):
    row, col = (new_y - 100) // cell_height, (new_x - 75) // cell_width
    if not start_goal:
        return 75 <= new_x <= 675 and 100 <= new_y <= 700 and grid_world[row][col] != 'X' \
            and grid_world[row][col] != 'G'
    else:
        return 75 <= new_x <= 675 and 100 <= new_y <= 700 and grid_world[row][col] != 'X' \
            and grid_world[row][col] != 'S'

def toggle_obstacle(pos, cell_width, cell_height, grid_world):
    x, y = pos
    col = (x - 75) // cell_width
    row = (y - 100) // cell_height

    if grid_world[row][col] == 'O':
        grid_world[row][col] = 'X'
    elif grid_world[row][col] == 'X':
        grid_world[row][col] = 'O'

def count_obstacles(grid_world):
    return sum(row.count('X') for row in grid_world)

