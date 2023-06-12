# 미세먼지 안녕! G4
import sys

input = sys.stdin.readline
r, c, t = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(r)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
air_top, air_bottom = 0, 0

# 공기청정기의 위치
for i in range(r):
    if arr[i][0] == -1:
        air_top = i
        air_bottom = i + 1
        break


def fine_dust():
    # 미세먼지 확산을 저장할 리스트
    spread = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if arr[i][j] > 0:
                tmp = 0
                # 인접한 방향으로 확산
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != -1:
                        spread[nx][ny] += arr[i][j] // 5  # 주변에 확산되는 양
                        tmp += arr[i][j] // 5  # (i, j)에서 빠지는 양
                arr[i][j] -= tmp  # 남은 미세먼지
    # 미세먼지 변동
    for i in range(r):
        for j in range(c):
            arr[i][j] += spread[i][j]


# 위쪽 공기청정기
def air_cleaner1():
    dir = 1  # 처음 방향인 오른쪽으로 진행
    before = 0  # 이전칸의 미세먼지양
    x, y = air_top, 1
    while True:
        # 한 방향으로 끝까지 이동
        nx = x + dx[dir]
        ny = y + dy[dir]
        # 경계에 닿으면 방향전환
        if nx == r or ny == c or nx == -1 or ny == -1:
            dir = (dir - 1) % 4
            continue
        # 위쪽 공기청정기 위치로 돌아오면 중지
        if x == air_top and y == 0:
            break
        # 한 칸씩 이동
        arr[x][y], before = before, arr[x][y]
        x, y = nx, ny


def air_cleaner2():
    dir = 1
    before = 0
    x, y = air_bottom, 1
    while True:
        nx = x + dx[dir]
        ny = y + dy[dir]
        if nx == r or ny == c or nx == -1 or ny == -1:
            dir = (dir + 1) % 4
            continue
        if x == air_bottom and y == 0:
            break
        arr[x][y], before = before, arr[x][y]
        x, y = nx, ny


for _ in range(t):
    fine_dust()
    air_cleaner1()
    air_cleaner2()

result = 2
for i in range(r):
    result += sum(arr[i])
print(result)
