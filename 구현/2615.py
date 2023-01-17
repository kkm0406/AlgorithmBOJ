# 오목 S1
import sys

input = sys.stdin.readline
arr = [list(map(int, input().split())) for i in range(19)]
# → ↓ ↘ ↗
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

for x in range(19):
    for y in range(19):
        if arr[x][y] != 0:
            color = arr[x][y]
            for i in range(4):
                cnt = 1
                nx = x + dx[i]
                ny = y + dy[i]

                while 0 <= nx < 19 and 0 <= ny < 19 and arr[nx][ny] == color:
                    cnt += 1
                    if cnt == 5:
                        # 제일 처음 좌표와 해당 좌표에서
                        # 한 칸(- dx[i], - dy[i]) 덜 이동한 좌표가 같은지
                        if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and arr[x - dx[i]][y - dy[i]] == color:
                            break
                        # 연속된 바둑알의 제일 마지막 좌표와
                        # 해당 좌표에서 한 칸(+ dx[i], + dy[i]) 더 이동한 좌표가 같은지
                        if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19 and arr[nx + dx[i]][ny + dy[i]] == color:
                            break
                        print(color)
                        print(x + 1, y + 1)
                        sys.exit(0)

                    nx += dx[i]
                    ny += dy[i]

print(0)
