# 농장 관리 G5

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
visited = [[False] * m for _ in range(n)]
dir = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
result = 0


def bfs(i, j):
    visited[i][j] = True
    q = deque([[i, j]])
    h = arr[i][j]  # 현재 위치의 높이
    flag = True
    while q:
        x, y = q.popleft()

        for dx, dy in dir:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m:
                # 미방문 동일 높이
                if not visited[nx][ny] and arr[nx][ny] == h:
                    q.append([nx, ny])
                    visited[nx][ny] = True
                # 인접한 격자 중 현재보다 높은 곳이 있으면 봉우리가 아님
                elif arr[nx][ny] > h:
                    flag = False

    if flag:
        return True
    else:
        return False


for i in range(n):
    for j in range(m):
        if not visited[i][j] and bfs(i, j):
            result += 1

print(result)
