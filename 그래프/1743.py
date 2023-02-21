# 음식물 피하기 S1
import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())
passage = [[0] * m for i in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = 0
visited = [[False] * m for i in range(n)]
for i in range(k):
    r, c = map(int, input().split())
    passage[r - 1][c - 1] = 1


def bfs(i, j):
    cnt = 1
    visited[i][j] = True
    q = deque()
    q.append([i, j])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 안에서 미방문한 곳에 음식물이 떨어져 있으면
            if 0 <= nx < n and 0 <= ny < m and passage[nx][ny] == 1:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append([nx, ny])
                    cnt += 1

    return cnt


for i in range(n):
    for j in range(m):
        if passage[i][j] == 1:  # 해당 위치에 음식물이 떨어져 있으면
            ans = max(ans, bfs(i, j))  # bfs 진행 후 음식물 크기 갱신

print(ans)
