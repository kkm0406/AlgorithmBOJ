# 오델로 S1
import sys

input = sys.stdin.readline
arr = [['.'] * 7 for i in range(7)]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
n = int(input())
arr[3][3] = arr[4][4] = 'W'
arr[3][4] = arr[4][3] = 'B'


def check(r, c, i, dir):
    nx, ny = r, c
    visited[nx][ny] = True
    if i % 2 == 0:  # 흑돌을 놓았을 때
        while 1:
            nx += dx[dir]  # 해당 방향으로 이동
            ny += dy[dir]
            # 맵 범위 나가면 break
            if nx < 1 or nx > 6 or ny < 1 or ny > 6:
                break
            # 방문했거나 빈 칸이면 break
            if visited[nx][ny] or arr[nx][ny] == '.':
                break
            # 탐색한 위치에 백돌이 있으면
            # 항상 상대방 돌을 양쪽에서 포위하여 뒤집을 수 있는 곳에 놓아야함
            if arr[nx][ny] == 'B':
                return True
            # 방문 처리
            visited[nx][ny] = True
    else:  # 백돌을 놓았을 때
        while 1:
            nx += dx[dir]
            ny += dy[dir]
            if nx < 1 or nx > 6 or ny < 1 or ny > 6:
                break
            if visited[nx][ny] or arr[nx][ny] == '.':
                break
            # 탐색 위치에 백돌이 있으면
            if arr[nx][ny] == 'W':
                return True
            visited[nx][ny] = True
    return False


def color(i):
    for j in range(1, 7):
        for k in range(1, 7):
            # 흑돌을 놓았을 때 방문한 곳이면
            if i % 2 == 0 and visited[j][k]:
                # 백돌로 뒤집힘
                arr[j][k] = 'B'
            elif i % 2 == 1 and visited[j][k]:
                arr[j][k] = 'W'


for i in range(n):
    r, c = map(int, input().split())
    for dir in range(8):
        # 돌을 놓은 위치에서 8방향으로 이동하며 탐색하기 때문에 매번 visited 배열 초기화
        visited = [[False] * 7 for i in range(7)]
        # 탐색
        if check(r, c, i, dir):
            color(i)

white, black = 0, 0
for i in range(1, 7):
    for j in range(1, 7):
        if arr[i][j] == 'B':
            black += 1
        elif arr[i][j] == 'W':
            white += 1
        print(arr[i][j], end="")
    print()

print("Black") if black > white else print("White")
