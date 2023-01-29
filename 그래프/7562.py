# 나이트의 이동 S1
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

dx = [2, 2, -2, -2, 1, -1, 1, -1]  # 나이트 x방향
dy = [1, -1, 1, -1, -2, -2, 2, 2]  # 나이트 y방향

t = int(input())


def bfs(x, y):
    q = deque()
    q.append([x, y])

    while q:
        x, y = q.popleft()
        for i in range(8):  # 나이트 이동 방향으로 bfs 진행
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 0:  # 새로 방문할 정점
                    graph[nx][ny] = graph[x][y] + 1
                    # (nx, ny)까지의 이동거리 = 이전까지 이동했던 거리 +1
                    q.append([nx, ny])


for _ in range(t):
    n = int(input())
    graph = [[0] * n for i in range(n)]
    x, y = map(int, input().split())
    movex, movey = map(int, input().split())
    if x == movex and y == movey:
        print(0)
    else:
        bfs(x, y)
        print(graph[movex][movey])
