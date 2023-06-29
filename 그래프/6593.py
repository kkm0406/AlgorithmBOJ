# 상범 빌딩 G5

import sys
from collections import deque

input = sys.stdin.readline
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def bfs():
    q = deque([[sx, sy, sz]])
    visited = [[[0] * c for _ in range(r)] for i in range(l)]
    visited[sx][sy][sz] = 0

    while q:
        x, y, z = q.popleft()

        if arr[x][y][z] == 'E':
            return f'Escaped in {visited[x][y][z]} minute(s).'

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < l and 0 <= ny < r and 0 <= nz < c and visited[nx][ny][nz] == 0:
                if arr[nx][ny][nz] == '.' or arr[nx][ny][nz] == 'E':
                    visited[nx][ny][nz] = visited[x][y][z] + 1
                    q.append([nx, ny, nz])

    return 'Trapped!'


while True:
    l, r, c = map(int, input().split())
    if l == r == c == 0:
        break

    arr = [[] * r for _ in range(l)]

    for i in range(l):
        for j in range(r):
            arr[i].append(list(input().strip()))
        input()

    sx, sy, sz = 0, 0, 0
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if arr[i][j][k] == 'S':
                    sx, sy, sz = i, j, k
                    break

    ans = bfs()
    print(ans)
