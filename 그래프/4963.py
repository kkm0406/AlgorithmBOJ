# 섬의 개수 S2
import sys
from collections import deque

input = sys.stdin.readline

# n, ne, e, se, s, sw, w, nw
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(8):  # 갈 수 있는 경로 탐색
            nx = x + dx[i]
            ny = y + dy[i]
            # 땅이면서 아직 방문 안했으면
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = []
    for i in range(h):
        graph.append(list(map(int, input().split())))

    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:  # 지도 탐색하면서 땅이면
                bfs(i, j)  # bfs 시작
                cnt += 1

    print(cnt)
