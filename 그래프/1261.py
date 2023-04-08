# 알고스팟 G4
import sys
from collections import deque

input = sys.stdin.readline
m, n = map(int, input().split())
arr = [list(map(int, input().rstrip())) for i in range(n)]
dist = [[-1] * m for i in range(n)]  # 벽을 깬 횟수 저장
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def bfs(i, j):
    q = deque()
    q.append([i, j])
    dist[i][j] = 0

    while q:
        x, y = q.popleft()
        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if dist[nx][ny] == -1:  # 해당 위치 방문하지 않았다면
                    if arr[nx][ny] == 0:  # 벽이 없으면
                        dist[nx][ny] = dist[x][y]  # 이전의 깬 횟수 저장
                        q.appendleft([nx, ny])  # 벽이 없는 곳을 우선 탐색해야 하므로 appendleft
                    else:  # 벽이 있으면
                        dist[nx][ny] = dist[x][y] + 1  # 이전의 깬 횟수 + 1
                        q.append([nx, ny])


bfs(0, 0)
print(dist[n - 1][m - 1])
