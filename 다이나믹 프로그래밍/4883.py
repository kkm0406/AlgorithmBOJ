# 삼각 그래프 S1

import sys

input = sys.stdin.readline

n = 1
while True:
    t = int(input())
    if t == 0:
        break
    arr = []
    for i in range(t):
        arr.append(list(map(int, input().split())))

    # 첫번째 행
    arr[1][0] += arr[0][1]
    arr[1][1] += min(arr[0][1], arr[0][1] + arr[0][2], arr[1][0])
    arr[1][2] += min(arr[0][1], arr[0][1] + arr[0][2], arr[1][1])

    # 층을 지날때 마다 최솟값을 찾음
    for i in range(2, t):
        arr[i][0] += min(arr[i - 1][0], arr[i - 1][1])
        arr[i][1] += min(arr[i - 1][0], arr[i - 1][1], arr[i - 1][2], arr[i][0])
        arr[i][2] += min(arr[i - 1][1], arr[i - 1][2], arr[i][1])

    print("%d. %d" % (n, arr[t - 1][1]))
    n += 1
