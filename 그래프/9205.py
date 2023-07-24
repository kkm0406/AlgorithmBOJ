# 맥주 마시면서 걸어가기 G5

import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    q = deque([[home[0], home[1]]])

    while q:
        x, y = q.popleft()
        # 현재 위치로부터 페스티벌까지 위치가 1000이하면
        # -> 50미터당 한병이므로 20*50m 이동가능
        if abs(x - festival[0]) + abs(y - festival[1]) <= 1000:
            print('happy')
            return
        for i in range(n):
            if not visited[i]:
                nx, ny = store[i]  # 편의점의 좌표
                # 현재 위치로부터 편의점의 좌표가 1000이하
                # -> 50미터당 한병이므로 20*50m 이동가능
                if abs(x - nx) + abs(y - ny) <= 1000:
                    visited[i] = True
                    q.append([nx, ny])
    print('sad')
    return


for _ in range(int(input())):
    n = int(input())
    home = list(map(int, input().split()))
    store = [list(map(int, input().split())) for i in range(n)]
    festival = list(map(int, input().split()))
    visited = [0 for i in range(n + 1)]
    bfs()
