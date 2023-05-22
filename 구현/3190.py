# 뱀 G4

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
# 우선 빈공간은 .로 표시
arr = [['.'] * (n + 1) for i in range(n + 1)]
k = int(input())
# 사과의 위치를 A로 표시
for i in range(k):
    a, b = map(int, input().split())
    arr[a][b] = 'A'

l = int(input())
# 딕셔너리로 시간과 이동방향을 저장
move = {}
for i in range(l):
    a, b = input().split()
    move[int(a)] = b

time = 0
# 동 -> 남 -> 서 -> 북
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
nx, ny = 1, 1  # 시작 위치
d = 0  # 초기 이동방향
snake = deque([[nx, ny]])  # 큐에 초기위치 저장
arr[nx][ny] = 'S'  # 뱀은 처음 (1, 1)에 위치

while True:
    time += 1
    # 방향에 맞게 계속 이동
    nx += dir[d][0]
    ny += dir[d][1]

    # 맵 벗어나면 break
    if nx > n or ny > n or nx < 1 or ny < 1:
        break

    # 이동한 위치에 사과가 있으면
    if arr[nx][ny] == 'A':
        # 해당 위치에 뱀표시
        arr[nx][ny] = 'S'
    else:
        # 없는데 뱀 표시가 있으면 몸통에 닿은 것
        if arr[nx][ny] == 'S':
            break
        # 빈 공간이면 꼬리위치 제거
        else:
            # 꼬리 위치 제거
            x, y = snake.popleft()
            arr[x][y] = '.'
            # 머리는 이동
            arr[nx][ny] = 'S'

    # 이동한 머리 좌표 추가
    snake.append([nx, ny])

    # 딕셔너리에 저장된 시간이면
    if time in move.keys():
        # 시계방향이동
        if move[time] == 'D':
            d = (d + 1) % 4
        # 반시계방향이동
        elif move[time] == 'L':
            d = (d - 1) % 4

print(time)
