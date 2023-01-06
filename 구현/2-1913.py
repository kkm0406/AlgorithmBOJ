# 달팽이 S3
import sys

N = int(sys.stdin.readline())
num = int(sys.stdin.readline())
dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # NRSL

arr = [[0] * N for i in range(N)]

initX = N // 2 # 시작 X
initY = N // 2 # 시작 T
start = 1 
arr[initX][initY] = start # 2차원 리스트 정가운데
for i in range(N // 2):
    way = "N" + "R" * (2 * i + 1) + "SS" * (i + 1) + "LL" * (i + 1) + "NN" * (i + 1)
    #N, R홀수번, SS짝수번, LL짝수번, NN짝수번 등장하는 규칙
    for j in way:
        nx, ny = 0, 0
        if j == 'N':
            nx = initX + dir[0][0]
            ny = initY + dir[0][1]
            #이동 방향에 따른 x, y 값 결정
        elif j == 'R':
            nx = initX + dir[1][0]
            ny = initY + dir[1][1]
        elif j == 'S':
            nx = initX + dir[2][0]
            ny = initY + dir[2][1]
        elif j == 'L':
            nx = initX + dir[3][0]
            ny = initY + dir[3][1]
        start += 1 #이동하면 값 증가
        arr[nx][ny] = start #이동한 위치 값 변경
        initX, initY = nx, ny #현위치 초기화

x, y = 0, 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == num:
            x, y = i, j
        print(arr[i][j], end=' ')
    print()

print(x + 1, y + 1)
