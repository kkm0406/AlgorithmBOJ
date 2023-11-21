# 미로 만들기 S2

import sys

input = sys.stdin.readline
n = int(input())
# 방향지정
dir = [(1, 0), (0, -1), (-1, 0), (0, 1)]
maze = [[0, 0]]  # 가는 위치
arr = list(input().strip())
dir_idx = 0  # 현재 방향
for move in arr:
    if move == 'R':  # 회전
        dir_idx = (dir_idx + 1) % 4
    elif move == 'L':  # 회전
        dir_idx = (dir_idx - 1) % 4
    else:
        # 이동 지점 maze에 저장
        x, y = maze[-1][0], maze[-1][1]
        x += dir[dir_idx][0]
        y += dir[dir_idx][1]
        maze.append([x, y])

# x, y좌표의 각각 최소 값 구함
min_x, min_y = 0, 0
for x, y in maze:
    min_x = min(min_x, x)
    min_y = min(min_y, y)

# 취소 위치만큼 이동 -> (0, 0)이 시작점이 되게
max_x, max_y = 0, 0
for i in range(len(maze)):
    maze[i][0] += abs(min_x)
    maze[i][1] += abs(min_y)
    # 이동한 maze의 최대 x, y -> 최종 지도의 크기
    max_x = max(maze[i][0], max_x)
    max_y = max(maze[i][1], max_y)

# 최종 지도 생성
maze_map = [["#"]*(max_y + 1) for j in range(max_x + 1)]

# 이동 위치에 .표시
for i, j in maze:
    maze_map[i][j] = '.'

for i in maze_map:
    print(''.join(i))
