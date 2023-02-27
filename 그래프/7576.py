# 토마토 G5
import sys
from collections import deque

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
m, n = map(int, input().split())
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
arr = [list(map(int, input().split())) for i in range(n)]
ans = 1e9
q = deque()


def bfs():
    while q:
        x, y = q.popleft()

        for dx, dy in dir:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                q.append((nx, ny))
                # 새로 익은 토마토는 이전 토마토 날짜 +1
                arr[nx][ny] = arr[x][y] + 1


for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            # 큐에 처음 토마토 위치를 append
            q.append((i, j))

bfs()
ans = 0
for i in arr:
    for j in i:
        if j == 0:  # 토마토가 안익었을 경우
            print(-1)
            exit(0)
    ans = max(ans, max(i))

# 시작일자가 1이므로 -1
print(ans - 1)
