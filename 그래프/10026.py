# 적록색약 G5
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

pic = [input().strip() for i in range(n)]  # 적록색약 x
pic_r = []  # 적록색약인 경우
for i in pic:
    tmp = i.replace('G', 'R')
    pic_r.append(tmp)

visited = [[False] * n for i in range(n)]
visited_r = [[False] * n for i in range(n)]
cnt, cnt_r = 0, 0
colors = ['R', 'B', 'G']
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def bfs(i, j, color):
    visited[i][j] = True
    q = deque()
    q.append([i, j])

    while q:
        x, y = q.popleft()

        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if pic[nx][ny] == color:
                    visited[nx][ny] = True
                    q.append([nx, ny])


def bfs_r(i, j, color):
    visited_r[i][j] = True
    q = deque()
    q.append([i, j])

    while q:
        x, y = q.popleft()

        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited_r[nx][ny]:
                if pic_r[nx][ny] == color:
                    visited_r[nx][ny] = True
                    q.append([nx, ny])


# 적록색약이 아닌 경우 bfs
for i in range(n):
    for j in range(n):
        for color in colors:
            if not visited[i][j] and pic[i][j] == color:
                bfs(i, j, color)
                cnt += 1

# 적록색약인 경우 bfs
for i in range(n):
    for j in range(n):
        for color in colors:
            if not visited_r[i][j] and pic_r[i][j] == color:
                bfs_r(i, j, color)
                cnt_r += 1

print(cnt, cnt_r)
