# 모노톤길 G5

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    tmp = [list(map(int, input().split())) for i in range(n)]
    arr = list(map(int, input().split()))
    arr = arr[1:]
    # 우선 x 좌표 기준 정렬
    tmp.sort(key=lambda x: x[0])
    coords = {}

    # x 좌표가 같은 지점끼리 묶음
    for x, y in tmp:
        if x not in coords:
            coords[x] = [y]
        else:
            coords[x].append(y)

    # 마지막 좌표와 가까운 거리순 정렬
    ex, ey = 0, 0
    for key, value in coords.items():
        if len(value) == 1:
            ex, ey = key, value[0]
        else:
            value.sort(key=lambda x: (abs(key - ex) + abs(x - ey)))
            ex, ey = key, value[-1]

    # 카페 번호: [x, y] 딕셔너리 생성
    cafe = {}
    idx = 1
    for key, value in coords.items():
        for i in value:
            cafe[idx] = [key, i]
            idx += 1

    for i in arr:
        print(*cafe[i])
