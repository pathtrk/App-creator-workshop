# 迷路ゲーム 作例

ゲームのアイディアを生成してもらい、そこからPythonプログラムも作成し、実行します。

## 実行例

1. 初期コードの実行
2. 迷路の複雑化
3. ゲームアプリ化



## 初期アイディアの生成

> Pythonで、簡単なゲームを作りたいです。初心者でも作れるゲームのアイデアを出してください。

*... アイディア 1. - 4. までを省略.しています...*

#### 5. **シンプルな迷路ゲーム**

**概要**: プレイヤーが文字ベースの迷路を上下左右に移動してゴールを目指す。

**ポイント**:

- 2次元リストを使って迷路を表現。
- プレイヤーの現在位置を更新して表示。

*... アイディア 5. - 7. までを省略しています...*



------

これらのアイデアの中で興味があるものを教えてください！コードの例やアドバイスも提供できます。



## 初期コードの実行

> ５. のシンプルな迷路ゲームに興味があります。具体的な作り方を教えてください。

シンプルな迷路ゲームの作り方をステップごとに説明します！文字ベースで迷路を作り、プレイヤーが上下左右に移動してゴールを目指す形にします。

------

#### **ステップ1: 迷路のデザイン**

迷路は2次元リストで表現します。
以下のように、`#`は壁、`.`は道、`P`はプレイヤーの初期位置、`G`はゴールです。

```python
maze = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "G", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", ".", ".", ".", "#"],
    ["#", "#", "#", "#", "#"]
]
```

------

#### **ステップ2: プレイヤーの位置を管理**

プレイヤーの現在位置を `(x, y)` のタプルで管理します。例えば、`(1, 1)` は上記迷路で `P` の位置です。

------

#### **ステップ3: 迷路を表示**

迷路を画面に表示する関数を作ります。プレイヤーの現在位置を考慮して動的に描画します。

```python
def display_maze(maze, player_pos):
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if (x, y) == player_pos:
                print("P", end="")  # プレイヤーの位置を表示
            else:
                print(maze[y][x], end="")
        print()
```

------

#### **ステップ4: プレイヤーを移動**

移動に応じてプレイヤーの位置を更新します。壁にぶつかる場合や迷路の外に出る場合は移動を無効にします。

```python
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
```

------

#### **ステップ5: ゲームループを作成**

プレイヤーがゴールに到達するまで移動を繰り返します。

```python
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
```

------

#### **完全版コード**

```python
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
```

------

### **カスタマイズのアイデア**

1. **迷路を大きくしたり複雑にする**
   迷路のデザインを変更して難易度を上げましょう。
2. **アイテムや罠を追加する**
   特定の位置にアイテムを置き、取得したらスコアが上がる仕組みを追加。
3. **時間制限をつける**
   `time` モジュールを使ってタイムアタック形式にする。

わからない部分や追加機能について相談があればぜひ聞いてください！

## 迷路の複雑化

> 迷路が単純すぎると感じました。自動で複雑な迷路を作るPythonプログラムを教えてください。

複雑な迷路を自動生成するPythonプログラムを以下に示します。アルゴリズムとして有名な「深さ優先探索 (Depth First Search, DFS)」を使って迷路を作成します。この方法は迷路が一本のつながった経路を持つ特徴的な構造を生成します。

------

#### **迷路生成プログラム**

以下のコードを使えば、自動的に複雑な迷路を作ることができます。

```python
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
```

------

#### **プログラムのポイント**

1. **迷路の初期化**:
   - 迷路は「#」で埋められた2次元リストとして初期化します。
   - 通路は「.」、スタート地点は「S」、ゴールは「G」とします。
2. **深さ優先探索 (DFS)**:
   - スタックを使って現在の位置から進める方向をランダムに探索します。
   - 通路を掘り進めるときは、隣接するマスを「.」に変更します。
3. **ランダムなゴールの配置**:
   - 掘り終わった後、右下に近い場所をゴール「G」に設定します。
4. **サイズについて**:
   - 迷路の幅と高さは奇数である必要があります。偶数の場合、迷路が正しく生成されません。

------

#### **出力例**

実行すると、次のような迷路が生成されます（例）。

```bash
#####################
#.....#.....#.....#G#
#.###.#.###.#.###.#.#
#.#...#.#...#...#.#.#
#.#.###.#.#####.#.#.#
#.#.....#.......#.#.#
#.###########.###.#.#
#.#...........#...#.#
#.#.###########.###.#
#.#.#.........#.#...#
#.#.#.#######.#.###.#
#.#.#.......#.#.#...#
#.#.#######.#.#.#.###
#.#.........#...#...#
#.#####.###########.#
#.#.....#...........#
#.#.#####.#########.#
#.#.......#.........#
#.#################.#
#...................#
#####################
```

------

#### **カスタマイズ案**

1. **迷路のサイズ変更**:
   - `width` と `height` を変更して迷路を拡大または縮小できます。
2. **ゴールやスタートの位置を固定**:
   - ゴールやスタート地点を明示的に設定することも可能です。
3. **複雑さの調整**:
   - `directions` の順序や探索ロジックを調整して迷路のパターンを変えられます。
4. **GUI化**:
   - `pygame` や `tkinter` を使えば、迷路をグラフィカルに表示して、ゲームとして遊べるように拡張可能です。

さらに改良や質問があれば教えてください！



## ゲームアプリ化

> ここまでの全てのコードがpygameで動くように修正してください

以下に、先ほどの迷路生成コードとプレイヤーが移動できるゲーム機能を統合した `pygame` バージョンを示します。これにより、迷路を `pygame` で描画し、プレイヤーを動かしてゴールを目指すことができるゲームが完成します。

------

#### **pygame バージョンコード**

```python
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
```

------

#### **コードの説明**

1. **迷路生成**
   - `create_maze` 関数でランダムな迷路を生成します。
   - スタート地点は (1, 1)、ゴール地点は右下に近い位置に自動配置されます。
2. **pygame の描画**
   - 各マスの状態に応じて色を変更します:
     - 壁 (`#`): 白
     - 通路 (`.`): 黒
     - ゴール (`G`): 緑
     - プレイヤー: 青
3. **プレイヤーの移動**
   - 矢印キー (`↑`, `↓`, `←`, `→`) を使用してプレイヤーを動かします。
   - プレイヤーは壁にぶつかるとその場にとどまります。
4. **ゴール到達**
   - プレイヤーがゴール地点に移動すると、メッセージを表示してゲームが終了します。

------

#### **カスタマイズ案**

1. **迷路サイズの変更**
   - `MAZE_WIDTH` と `MAZE_HEIGHT` を調整して迷路を拡大・縮小できます。
2. **タイムアタック**
   - 開始時刻を記録し、ゴール到達時にクリアタイムを表示する機能を追加できます。
3. **敵キャラの追加**
   - ランダムに動く敵キャラを追加して難易度を上げることができます。
4. **レベルシステム**
   - ゴール到達後に新しい迷路を生成し、レベルアップする仕組みを作成できます。

楽しんでください！質問があればいつでもどうぞ！

