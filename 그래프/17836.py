# 공주님을 구해라! G5

import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]


def bfs(i, j):
    q = deque([[i, j]])
    visited = [[0] * m for _ in range(n)]
    visited[i][j] = 1
    dist = 1e9
    while q:
        x, y = q.popleft()
        if arr[x][y] == 2:  # 그람획득시 -> 벽 상관 x
            # (n-1, m-1)까지 바로 이동하는 거리
            dist_x = abs(x - (n - 1))
            dist_y = abs(y - (m - 1))
            dist = visited[x][y] - 1 + dist_x + dist_y
        if x == n - 1 and y == m - 1:  # 그람있을 때와 없을 때 비교
            return min(dist, visited[x][y] - 1)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != 1:
                if visited[nx][ny] == 0:
                    q.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1

    return dist


result = bfs(0, 0)
print("Fail" if result > t else result)
