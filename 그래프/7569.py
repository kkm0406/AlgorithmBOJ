# 토마토 G5
import sys
from collections import deque

input = sys.stdin.readline
m, n, h = map(int, input().split())
dir = [(-1, 0, 0), (1, 0, 0), (0, 1, 0),
       (0, -1, 0), (0, 0, 1), (0, 0, -1)]
arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
q = deque()

for k in range(h):
    for i in range(n):
        for j in range(m):
            # 익은 토마토는 큐에 저장
            if arr[k][i][j] == 1:
                q.append((k, i, j))

# bfs 진행
while q:
    z, x, y = q.popleft()

    for dx, dy, dz in dir:
        nx, ny, nz = x + dx, y + dy, z + dz
        if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and arr[nz][nx][ny] == 0:
            q.append((nz, nx, ny))
            # 익은날짜는 전의 토마토+1
            arr[nz][nx][ny] = arr[z][x][y] + 1

result = 0
for k in range(h):
    for i in range(n):
        for j in range(m):
            #안익은 토마토가 있으면
            if arr[k][i][j] == 0:
                print(-1)
                sys.exit(0)
            result = max(result, arr[k][i][j])

print(result - 1)
