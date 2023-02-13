# 미로 탐색 S1
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for i in range(n)]
cnt = 0
visited = [[False] * m for i in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(sx, sy):
    global cnt
    q = deque()
    q.append([sx, sy])
    visited[sx][sy] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                # 범위안에서 방문안한 칸일 때
                if arr[nx][ny] == 1:  # 이동할 수 있는 칸디면
                    visited[nx][ny] = True
                    q.append([nx, ny])
                    arr[nx][ny] += arr[x][y]  # 이전경로 +1로 갱신


bfs(0, 0)
print(arr[n - 1][m - 1])
