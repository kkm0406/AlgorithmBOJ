# 미로만들기 G4
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dist = [[-1] * n for _ in range(n)]  # 방의 색을 바꾸는 횟수 저장


def bfs(i, j):
    dist[i][j] = 0
    q = deque()
    q.append([i, j])

    while q:
        x, y = q.popleft()
        for dx, dy in dir:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:  # 방문 안한 정점
                if arr[nx][ny] == 1:  # 흰색 방이면
                    dist[nx][ny] = dist[x][y]  # 바꾼 횟수 유지
                    q.appendleft([nx, ny])  # 흰색 방 우선 탐색 -> appendleft
                else:  # 검은색 방이면
                    dist[nx][ny] = dist[x][y] + 1  # 바꾼횟수+1
                    q.append([nx, ny])


bfs(0, 0)
print(dist[n - 1][n - 1])
