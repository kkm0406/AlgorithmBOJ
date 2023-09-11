# 탈출 G4

import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())
arr = [list(input().strip()) for i in range(r)]
# 방문 여부
visited = [[False] * c for _ in range(r)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
sx, sy = 0, 0

for i in range(r):
    for j in range(c):
        if arr[i][j] == 'S':
            sx, sy = i, j

# 처음 고슴도치 위치를 큐에 삽입
q = deque([[sx, sy]])
visited[sx][sy] = True
move = 0  # 이동횟수

while q:
    water = []
    # 물의 좌표 저장
    for i in range(r):
        for j in range(c):
            if arr[i][j] == '*' and not visited[i][j]:
                water.append([i, j])
                visited[i][j] = True

    # 홍수 구현
    for x, y in water:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                if arr[nx][ny] == '.':
                    arr[nx][ny] = '*'

    # 고슴도치 이동횟수 증가
    move += 1

    # 큐 저장된 모든 좌표에서 이동 -> 고슴도치가 이동할 수 있는 모든 위치 탐색
    for _ in range(len(q)):
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                if arr[nx][ny] == '.':
                    visited[nx][ny] = True
                    q.append([nx, ny])
                elif arr[nx][ny] == 'D':
                    print(move)
                    exit()

print("KAKTUS")
