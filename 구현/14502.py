# 연구소 G4

from collections import deque
import copy
import sys
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
result = 0
wall = []  # 벽을 세울수 있는 위치 저장
virus = []  # 초기 바이러스 위치 저장

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            wall.append((i, j))  # 벽을 세울 수 있는 위치 저장
        if arr[i][j] == 2:
            virus.append((i, j))  # 초기 바이러스 위치 저장

wall_combi = list(combinations(wall, 3))  # 벽을 세울 수 있는 조합 생성


def bfs(i, j):
    q = deque()
    q.append((i, j))

    while q:
        x, y = q.popleft()

        for dx, dy in dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and tmp_arr[nx][ny] == 0:
                q.append((nx, ny))
                tmp_arr[nx][ny] = 2

    return


for combi in wall_combi:  # 벽을 세울 수 있는 조합에서
    tmp_arr = copy.deepcopy(arr)  # tmp배열 복사
    for x, y in combi:  # 벽 세우기
        tmp_arr[x][y] = 1

    for i, j in virus:  # 초기 바이러스 위치에서 bfs 진행
        bfs(i, j)

    # 안전 영역 크기 구하기
    area = 0
    for i in range(n):
        for j in range(m):
            if tmp_arr[i][j] == 0:
                area += 1

    if result < area:
        result = area

print(result)
