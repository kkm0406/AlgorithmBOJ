# 유성 S1

import sys
from collections import deque

input = sys.stdin.readline

r, s = map(int, input().split())

arr = [list(input().strip()) for i in range(r)]
cnt = 1e9

for i in range(s):
    star, ground = 0, 0  # 가장 높은 유성 위치, 가장 낮은 땅 위치
    for j in range(r):  # j번째 행을 살펴보면서
        if arr[j][i] == 'X':
            star = j + 1
        elif arr[j][i] == '#':
            ground = j + 1
            break
    if star != 0 and ground != 0:
        # 유성와 땅까지의 거리 중 최솟값
        cnt = min(cnt, ground - star - 1)

for j in range(s):
    for i in range(r - 1, -1, -1):
        # 유성이면 좌표 변경 -> cnt만큼 배여 ㄹ이동
        if arr[i][j] == 'X':
            arr[i + cnt][j] = 'X'
            arr[i][j] = '.'

for i in arr:
    print(''.join(i))
