# 인구 이동 G5
import sys
from collections import deque

input = sys.stdin.readline
n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(i, j):
    q = deque()
    q.append([i, j])
    border = set()  # 국경선을 공유하는 나라 좌표
    border.add((i, j))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(arr[x][y] - arr[nx][ny]) <= r:
                    q.append([nx, ny])
                    visited[nx][ny] = True
                    border.add((nx, ny))  # 국경을 공유하면 추가

    return border


time = 0
while True:
    visited = [[False] * n for i in range(n)]
    flag = False  # 인구 이동 여부
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                border = bfs(i, j)
                if len(border) > 1:  # 국경을 공유하는 나라 2개 이상 -> 국경선 개방
                    flag = True
                    # 이동하는 총 인구
                    people = 0
                    for x, y in border:
                        people += arr[x][y]
                        # 인구 이동
                    for x, y in border:
                        arr[x][y] = int(people / len(border))

    if not flag:
        break

    time += 1

print(time)
