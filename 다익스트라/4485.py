# 녹색 옷 입은 애가 젤다지? G4
import heapq
import sys

input = sys.stdin.readline
inf = sys.maxsize
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dijkstra(i, j):
    q = []
    # 시작위치의 도둑루피
    heapq.heappush(q, (arr[i][j], i, j))
    distance[i][j] = arr[i][j]
    while q:
        dist, x, y = heapq.heappop(q)
        if dist > distance[x][y]:
            continue
        for i in range(4):  # 상하좌우 인접방향 이동
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:  # 범위 내에 있으면
                cost = arr[nx][ny] + dist  # 인접방향까지의 이동거리
                if cost < distance[nx][ny]:  # 해당 경우의 이동거리가 더 짧으면 갱신
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))


cnt = 1
while True:
    n = int(input())
    if n == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(n)]
    # 2차원 리스트의 최단거리 테이블
    distance = [[inf] * n for _ in range(n)]
    dijkstra(0, 0)
    print("Problem {}: {}".format(cnt, distance[-1][-1]))
    cnt += 1
