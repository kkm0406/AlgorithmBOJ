# 양 S1

import sys
from collections import deque

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
r, c = map(int, input().split())
arr = [list(input().rstrip()) for i in range(r)]
visited = [[False] * c for i in range(r)]
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
o, v = 0, 0
# 전체 양, 늑대 수 세기
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'o':
            o += 1
        elif arr[i][j] == 'v':
            v += 1


# 시작점 주변 영역 탐색
def bfs(i, j):
    global o, v
    q = deque([[i, j]])
    visited[i][j] = True
    # 영역 내 양, 늑대 수
    tmp_o, tmp_v = 0, 0
    # 시작점이 양이나 늑대면 추가
    if arr[i][j] == 'o':
        tmp_o += 1
    elif arr[i][j] == 'v':
        tmp_v += 1
    while q:
        x, y = q.popleft()

        for dx, dy in dir:
            nx = x + dx
            ny = y + dy

            # 범위 내 미방문 지점이면
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                if arr[nx][ny] == 'o':
                    tmp_o += 1
                elif arr[nx][ny] == 'v':
                    tmp_v += 1
                # 벽 만나면 continue
                elif arr[nx][ny] == '#':
                    continue
                visited[nx][ny] = True
                q.append([nx, ny])

    # 영역 내 양, 늑대 수 보고 판단
    if tmp_o > tmp_v:
        v -= tmp_v
    else:
        o -= tmp_o


for i in range(r):
    for j in range(c):
        # 미방문 && 벽이 아니면 bfs 진행
        if not visited[i][j] and arr[i][j] != "#":
            bfs(i, j)

print(o, v)
