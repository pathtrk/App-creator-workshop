def display_maze(maze, player_pos):
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if (x, y) == player_pos:
                print("P", end="")  # プレイヤーの位置を表示
            else:
                print(maze[y][x], end="")
        print()

def move_player(maze, player_pos, direction):
    x, y = player_pos
    if direction == "w":  # 上
        new_pos = (x, y - 1)
    elif direction == "s":  # 下
        new_pos = (x, y + 1)
    elif direction == "a":  # 左
        new_pos = (x - 1, y)
    elif direction == "d":  # 右
        new_pos = (x + 1, y)
    else:
        return player_pos  # 無効な入力の場合はそのまま
    
    # 新しい位置が道であれば移動、そうでなければ元の位置
    if maze[new_pos[1]][new_pos[0]] != "#":
        return new_pos
    return player_pos

def play_maze_game():
    maze = [
        ["#", "#", "#", "#", "#"],
        ["#", ".", ".", "G", "#"],
        ["#", ".", "#", ".", "#"],
        ["#", ".", ".", ".", "#"],
        ["#", "#", "#", "#", "#"]
    ]
    player_pos = (1, 1)  # 初期位置

    while True:
        display_maze(maze, player_pos)
        move = input("移動 [w:上, s:下, a:左, d:右]: ").strip()
        player_pos = move_player(maze, player_pos, move)

        # ゴールに到達したら終了
        if maze[player_pos[1]][player_pos[0]] == "G":
            print("ゴールに到達しました！おめでとう！")
            break

# ゲーム開始
play_maze_game()
