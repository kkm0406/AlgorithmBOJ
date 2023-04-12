# 아기 상어 G3
import sys
from collections import deque
import heapq

input = sys.stdin.readline
n = int(input())
baby_x = baby_y = 0
size = 2
eat = 0
arr = [list(map(int, input().split())) for i in range(n)]
time = 0
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            baby_x, baby_y = i, j  # 아기 상어 위치


def bfs(i, j, size):
    visited = [[-1] * n for i in range(n)]  # 아기상어까지의 거리
    q = deque()
    q.append([i, j])
    visited[i][j] = 0
    fish = []  # 아기상어가 먹을 수 있는 물고기
    while q:
        x, y = q.popleft()

        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:  # 미방문한 정점이면
                if arr[nx][ny] <= size:  # 아기상어 크기 이하이면 움직일 수 있음
                    q.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1  # 거리+1
                    if 0 < arr[nx][ny] < size:  # 먹을 수 있으면
                        fish.append([visited[nx][ny], nx, ny])  # 리스트에 추가

    return sorted(fish, key=lambda x: (x[0], x[1], x[2]))  # 거리순, x좌표, y좌표 순으로 정렬


while True:
    fish = bfs(baby_x, baby_y, size)  # 현재 아기상어가 먹을 수 있는 물고기 리스트
    if not fish:  # 없으면 종료
        break
    dist, x, y = fish[0]  # 아기 상어가 먹을 물고기
    time += dist  # 이동시간 추가
    arr[x][y] = arr[baby_x][baby_y] = 0  # 먹은 칸, 아기 상어 칸 빈칸으로
    baby_x, baby_y = x, y  # 먹은 칸으로 아기 상어 이동
    eat += 1  # 물고기 먹은 횟수
    if eat == size:  # 아기 상어 크기만큼 먹었으면
        size += 1  # 사이즈 증가
        eat = 0  # 먹은 횟수 초기화

print(time)
