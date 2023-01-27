# 유기농 배추 S2
import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
t = int(input())


def bfs(i, j):
    q = deque()
    q.append([i, j])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                q.append([nx, ny])
                graph[nx][ny] = 0


for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for i in range(n)]
    for i in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    cnt = 0
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 1:  # 배추가 심어져 있으면 BFS 진행
                bfs(x, y)
                cnt += 1

    print(cnt)
