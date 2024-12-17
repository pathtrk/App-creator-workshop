import random

def create_maze(width, height):
    # 迷路の初期化
    maze = [["#" for _ in range(width)] for _ in range(height)]
    
    # スタート位置をランダムに決定 (奇数のみ)
    start_x, start_y = 1, 1
    maze[start_y][start_x] = "."
    
    # スタックを使った深さ優先探索
    stack = [(start_x, start_y)]
    directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]  # 上, 下, 左, 右

    while stack:
        current_x, current_y = stack[-1]
        random.shuffle(directions)  # 移動方向をランダムに並べ替え
        moved = False

        for dx, dy in directions:
            next_x, next_y = current_x + dx, current_y + dy
            if 1 <= next_x < width - 1 and 1 <= next_y < height - 1 and maze[next_y][next_x] == "#":
                # 壁を壊して通路を作る
                maze[current_y + dy // 2][current_x + dx // 2] = "."
                maze[next_y][next_x] = "."
                stack.append((next_x, next_y))
                moved = True
                break
        
        if not moved:
            stack.pop()

    # ゴールを設定（ランダムな位置）
    goal_set = False
    for y in range(height - 1, 0, -1):
        for x in range(width - 1, 0, -1):
            if maze[y][x] == ".":
                maze[y][x] = "G"
                goal_set = True
                break
        if goal_set:
            break

    return maze

def print_maze(maze):
    for row in maze:
        print("".join(row))

# 迷路のサイズ
width, height = 21, 21  # 奇数サイズにすること
maze = create_maze(width, height)
print_maze(maze)
