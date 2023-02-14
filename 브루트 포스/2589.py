# 보물섬 G5
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(input().strip()) for i in range(n)]
dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]


def bfs(i, j):
    q = deque()
    q.append([i, j])
    visited = [[0] * m for i in range(n)]  # 방문했는지 여부 저장
    visited[i][j] = 1  # 처음 보물이 묻힌 곳 방문 처리
    cnt = 0
    while q:
        x, y = q.popleft()
        for dx, dy in dir:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] == 'L':
                # 범위 내, 미방문, 보물이 있으면
                visited[nx][ny] = visited[x][y] + 1  # 거리 추가
                if cnt < visited[nx][ny]:  # 최단거리 최신화
                    cnt = visited[nx][ny]
                q.append([nx, ny])

    return cnt - 1  # 처음 방문했던곳 재방문하기 때문에 -1


ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':  # 보물이 있으면
            tmp = bfs(i, j)  # BFS 진행
            if ans < tmp:
                ans = tmp

print(ans)
