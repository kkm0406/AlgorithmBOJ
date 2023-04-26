# 마법사 상어와 비바라기 G5
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
moves = [list(map(int, input().split())) for i in range(m)]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
clouds = [[n - 2, 0], [n - 2, 1], [n - 1, 0], [n - 1, 1]]
cx = [-1, -1, 1, 1]
cy = [-1, 1, -1, 1]

for d, s in moves:
    new_clouds = []

    # 모든 구름이 d방향 s칸 이동
    for x, y in clouds:
        # 1번 행, 열과 n번 행, 열이 연결되어 있으므로 모듈러 연산필요
        nx = (x + dx[d - 1] * s) % n
        ny = (y + dy[d - 1] * s) % n
        new_clouds.append([nx, ny])  # 구름이 이동한 위치

    # 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양 1증가
    visited = [[False] * n for _ in range(n)]
    for x, y in new_clouds:
        arr[x][y] += 1
        visited[x][y] = True  # 구름이 생긴 칸에 다시 구름이 생기면 안됨

    # 구름이 모두 사라짐
    clouds.clear()

    # 물복사버그 마법
    for x, y in new_clouds:
        cnt = 0
        # 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 바구니의 물이 증가
        for i in range(4):
            nx = x + cx[i]
            ny = y + cy[i]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] > 0:
                cnt += 1
        arr[x][y] += cnt

    # 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다.
    # 이 떄, 구름이 생기는 칸은 3에서 구름이 사라진 칸 x
    for i in range(n):
        for j in range(n):
            if arr[i][j] >= 2 and not visited[i][j]:
                arr[i][j] -= 2
                clouds.append([i, j])

result = 0
for i in arr:
    result += sum(i)

print(result)
