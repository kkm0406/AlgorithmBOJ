# 영역 구하기 S1
import sys
from collections import deque

input = sys.stdin.readline
m, n, k = map(int, input().split())
arr = [[1] * n for i in range(m)]
visited = [[False] * n for i in range(m)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = 0

cnt = 0
area = []


def bfs(i, j):
    q = deque()
    q.append([i, j])
    visited[i][j] = True
    size = 1

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]

            if 0 <= ny < m and 0 <= nx < n and arr[ny][nx] == 1:
                if not visited[ny][nx]:
                    size += 1
                    visited[ny][nx] = True
                    q.append([ny, nx])
                    arr[ny][nx] = 0

    return size


for i in range(m):
    for j in range(n):
        if arr[i][j] == 1:
            arr[i][j] = 0
            area.append(bfs(i, j))

            cnt+=1

area.sort()
print(cnt)
print(*area)
