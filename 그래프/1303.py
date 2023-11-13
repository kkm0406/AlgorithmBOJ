# 전쟁 - 전투 S1

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(input().strip()) for i in range(m)]
b, w = 0, 0
visited = [[False] * n for _ in range(m)]


def bfs(i, j, color):
    global b, w
    visited[i][j] = True
    q = deque()
    q.append([i, j])
    cnt = 1
    while q:
        x, y = q.popleft()
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                if arr[nx][ny] == color:  # 시작한 색과 같을때 이어서 탐색
                    q.append([nx, ny])
                    visited[nx][ny] = True
                    cnt += 1
    return cnt ** 2


for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            result = bfs(i, j, arr[i][j])
            if arr[i][j] == 'W':
                w += result
            else:
                b += result

print(w, b)
