# 그림 S1
import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(int, input().split())) for i in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 0
result = 0


def bfs(i, j):
    q = deque()
    q.append((i, j))
    area = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 1:
                    area += 1
                    board[nx][ny] = 0
                    q.append((nx, ny))

    if area == 0:
        # 색칠된 부분이 하나인 경우 area = 0
        return 1
    else:
        return area


for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            result = max(bfs(i, j), result)
            cnt += 1

print(cnt)
print(result)
