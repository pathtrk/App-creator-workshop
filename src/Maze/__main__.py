import pygame
import random
import sys

# 迷路生成関数
def create_maze(width, height):
    maze = [["#" for _ in range(width)] for _ in range(height)]
    start_x, start_y = 1, 1
    maze[start_y][start_x] = "."
    stack = [(start_x, start_y)]
    directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]

    while stack:
        current_x, current_y = stack[-1]
        random.shuffle(directions)
        moved = False

        for dx, dy in directions:
            next_x, next_y = current_x + dx, current_y + dy
            if 1 <= next_x < width - 1 and 1 <= next_y < height - 1 and maze[next_y][next_x] == "#":
                maze[current_y + dy // 2][current_x + dx // 2] = "."
                maze[next_y][next_x] = "."
                stack.append((next_x, next_y))
                moved = True
                break

        if not moved:
            stack.pop()

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

# pygame の初期設定
pygame.init()

# 迷路設定
TILE_SIZE = 20
MAZE_WIDTH, MAZE_HEIGHT = 21, 21  # 必ず奇数にする
SCREEN_WIDTH, SCREEN_HEIGHT = MAZE_WIDTH * TILE_SIZE, MAZE_HEIGHT * TILE_SIZE

# 色設定
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# プレイヤー移動
def move_player(player_pos, direction, maze):
    x, y = player_pos
    if direction == "UP" and maze[y - 1][x] in (".", "G"):
        return (x, y - 1)
    if direction == "DOWN" and maze[y + 1][x] in (".", "G"):
        return (x, y + 1)
    if direction == "LEFT" and maze[y][x - 1] in (".", "G"):
        return (x - 1, y)
    if direction == "RIGHT" and maze[y][x + 1] in (".", "G"):
        return (x + 1, y)
    return player_pos

# ゲームメインループ
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Maze Game")
    clock = pygame.time.Clock()

    maze = create_maze(MAZE_WIDTH, MAZE_HEIGHT)
    player_pos = (1, 1)  # 初期位置

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player_pos = move_player(player_pos, "UP", maze)
        if keys[pygame.K_DOWN]:
            player_pos = move_player(player_pos, "DOWN", maze)
        if keys[pygame.K_LEFT]:
            player_pos = move_player(player_pos, "LEFT", maze)
        if keys[pygame.K_RIGHT]:
            player_pos = move_player(player_pos, "RIGHT", maze)

        # ゴールに到達した場合
        if maze[player_pos[1]][player_pos[0]] == "G":
            print("ゴールに到達しました！おめでとう！")
            running = False

        # 描画
        screen.fill(BLACK)
        for y in range(MAZE_HEIGHT):
            for x in range(MAZE_WIDTH):
                rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                if maze[y][x] == "#":
                    pygame.draw.rect(screen, WHITE, rect)
                elif maze[y][x] == "G":
                    pygame.draw.rect(screen, GREEN, rect)
                else:
                    pygame.draw.rect(screen, BLACK, rect)

        # プレイヤーを描画
        player_rect = pygame.Rect(player_pos[0] * TILE_SIZE, player_pos[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(screen, BLUE, player_rect)

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()
    sys.exit()

# ゲーム開始
if __name__ == "__main__":
    main()
